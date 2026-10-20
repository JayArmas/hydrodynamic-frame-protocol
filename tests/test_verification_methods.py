"""Negative controls and boundary checks for the verification machinery."""
from pathlib import Path
import importlib.util
import json
import subprocess
import shutil
import sys
import tempfile
import unittest
import sympy as S

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("protocol_verifier",ROOT/"scripts/verify_protocol.py")
V=importlib.util.module_from_spec(spec)
spec.loader.exec_module(V)
s,q,k=V.s,V.q,V.k

class VerificationMethods(unittest.TestCase):
    def test_known_strict_real_polynomials(self):
        self.assertTrue(all(x>0 for x in V.hurwitz((s+1)*(s+2)*(s+3))))
        self.assertLess(V.hurwitz(s-1)[0],0)

    def test_zero_minors_do_not_prove_stability(self):
        self.assertEqual(V.hurwitz(s*s-1),[0,0])
        self.assertEqual((s*s-1).subs(s,1),0)

    def test_marginal_shift(self):
        epsilon=S.symbols("epsilon",positive=True)
        self.assertTrue(all(x.is_positive for x in V.hurwitz((s+epsilon)**2+1)))
        self.assertLess(S.limit(V.hurwitz((s+epsilon)**2-1)[-1]/epsilon,epsilon,0),0)

    def test_coefficient_conjugate_product(self):
        def product(p):return S.expand(p*sum(S.conjugate(a)*s**j for (j,),a in S.Poly(p,s).terms()))
        self.assertTrue(all(x>0 for x in V.hurwitz(product(s+1+2*S.I))))
        self.assertTrue(any(x<0 for x in V.hurwitz(product(s-1+2*S.I))))

    def test_wrong_factor_remainder_is_rejected(self):
        self.assertNotEqual(S.rem((s+1)*(s+2),s+3,s),0)
        with self.assertRaises(AssertionError):V.check("negative_control_remainder",S.rem((s+1)*(s+2),s+3,s))

    def test_zero_remainder_does_not_fix_normalization(self):
        polynomial=2*(s+1)*(s+2)
        self.assertEqual(S.rem(polynomial,s+1,s),0)
        self.assertNotEqual(S.expand(polynomial-(s+1)*(s+2)),0)

    def test_epsilon2_zero_alone_does_not_give_relaxation_factor(self):
        c=dict(e1=S.Integer(3),e2=0,p1=2,p2=0,t1=1,t2=1,eta=S.Integer(1))
        polynomial=V.poly_from_matrix(V.neutral(S.Integer(2),S.Rational(1,3),c),S.Rational(1,3))
        self.assertNotEqual(S.rem(polynomial,s+2,s),0)

    def test_entropy_changes_when_bulk_frame_coefficient_is_changed(self):
        th=dict(T=S.Integer(1),r=0,A=S.Rational(1,3),B=1)
        c={key:S.S.Zero for key in ("e1","e2","e3","p1","p2","p3","nu1","nu2","nu3","t1","t2","t3","ga1","ga2","ga3")}
        changed=c|{"p2":S.Integer(1)}
        self.assertEqual(V.entropy(th,changed)["bulk"]-V.entropy(th,c)["bulk"],-1)

    def test_standard_double_telegrapher_cannot_match_neutral_ideal_term(self):
        self.assertEqual(S.expand((s*s+s+q)*(2*s*s+s+3*q)).subs(s,0).coeff(q,1),0)
        self.assertNotEqual((S.Rational(1,3)*4*q).coeff(q,1),0)

    def test_zero_transport_changes_degree(self):
        D,tau=S.symbols("D tau",nonnegative=True)
        p=tau*s*s+s+D*q
        self.assertEqual(S.Poly(p.subs({D:0,tau:0}),s).degree(),1)
        self.assertEqual(S.factor(p.subs(D,0)),s*(s*tau+1))

    def test_examples_use_no_binary_floats(self):
        def inspect(obj):
            self.assertNotIsInstance(obj,float)
            if isinstance(obj,dict):
                for item in obj.values():inspect(item)
            if isinstance(obj,list):
                for item in obj:inspect(item)
        inspect(json.loads((ROOT/"examples/inputs.json").read_text()))

    def test_output_cannot_overwrite_frozen_reference(self):
        result=subprocess.run([sys.executable,"-B",str(ROOT/"scripts/verify_protocol.py"),"--output",str(ROOT/"reference_results")],capture_output=True,text=True)
        self.assertNotEqual(result.returncode,0)
        self.assertIn("output must be a new directory",result.stderr)

    def test_invalid_physical_transport_saves_failure_evidence(self):
        with tempfile.TemporaryDirectory(prefix="bdnk-negative-control-") as temp:
            isolated=Path(temp)
            for directory in ("scripts","examples","generated"):
                (isolated/directory).mkdir()
            shutil.copyfile(ROOT/"scripts/verify_protocol.py",isolated/"scripts/verify_protocol.py")
            inputs=json.loads((ROOT/"examples/inputs.json").read_text())
            inputs["cases"][0]["eta"]="-1"
            (isolated/"examples/inputs.json").write_text(json.dumps(inputs))
            output=isolated/"generated/failing-run"
            result=subprocess.run([sys.executable,"-I","-B",str(isolated/"scripts/verify_protocol.py"),"--output",str(output)],capture_output=True,text=True)
            self.assertNotEqual(result.returncode,0)
            failure=json.loads((output/"failure.json").read_text())
            self.assertFalse(failure["exact_requirements"]["conformal_benchmark_physical_eta"])
            self.assertFalse((output/"verification.json").exists())
            self.assertNotIn("PASS:",(output/"run.log").read_text())

    def test_degree_counts_include_q_weight_two(self):
        p=(s*s+s+q)**2*(s**4+s**3+s*s*q+q+q*q)
        poly=S.Poly(S.expand(p),s,q)
        self.assertEqual(poly.degree(s),8)
        self.assertEqual(max(a+2*b for (a,b),coef in poly.terms()),8)

if __name__=="__main__":unittest.main()
