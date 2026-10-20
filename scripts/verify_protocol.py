#!/usr/bin/env python3
"""Reproduce selected protocol identities from explicitly assembled matrices.

This is a teaching certificate for algebra and finite diagnostic examples,
not certification of a new family or of a new physical system. No manuscript
or historical result is written. Run from any directory with SymPy installed.
"""
from pathlib import Path
import hashlib
import json
import platform
import re
import sys
import argparse
import traceback
from datetime import datetime, timezone
import mpmath

import sympy as S

ROOT = Path(__file__).resolve().parents[1]
checks = {}
requirements = {}
RUN_OUTPUT = None
s, q, k = S.symbols("s q k", real=True)


def encode(obj):
    if isinstance(obj, dict):
        return {str(a): encode(b) for a, b in obj.items()}
    if isinstance(obj, (tuple, list)):
        return [encode(a) for a in obj]
    if isinstance(obj, S.MatrixBase):
        return [[str(v) for v in row] for row in obj.tolist()]
    if isinstance(obj, S.Basic):
        return str(obj)
    return obj


def check(name, residual):
    value = S.factor(residual)
    checks[name] = str(value)
    if value != 0:
        raise AssertionError(f"{name}: {value}")


def require(name, condition):
    """Exact Boolean checks, separate from zero-residual identities."""
    requirements[name] = bool(condition)
    if condition is not S.true and condition is not True:
        raise AssertionError(f"{name}: {condition}")


def neutral(w, x, c):
    e1, e2, p1, p2, t1, t2, eta = [c[a] for a in
        ("e1", "e2", "p1", "p2", "t1", "t2", "eta")]
    return S.Matrix([
        [e1*s**2+w*s/x-t2*k**2, S.I*k*(w+(e2+t1)*s)],
        [S.I*k*(w+(t2+p1)*s), t1*s**2+w*s+(4*eta/3-p2)*k**2]])


def charged(th, c):
    T, w, n, E, F, N, H = [th[a] for a in ("T", "w", "n", "E", "F", "N", "H")]
    return S.Matrix([
        [E*s+c["e1"]*s**2/T-c["t2"]*k**2/T,
         F*s+c["e3"]*s**2-c["t3"]*k**2,
         S.I*k*(w+(c["e2"]+c["t1"])*s)],
        [S.I*k*(w/T+(c["t2"]+c["p1"])*s/T),
         S.I*k*(T*n+(c["t3"]+c["p3"])*s),
         c["t1"]*s**2+w*s+(4*c["eta"]/3-c["p2"])*k**2],
        [N*s+c["nu1"]*s**2/T-c["ga2"]*k**2/T,
         H*s+c["nu3"]*s**2-c["ga3"]*k**2,
         S.I*k*(n+(c["nu2"]+c["ga1"])*s)]])


def uplift(th, c, diffusion, tau):
    T, r, qt, qa = [th[a] for a in ("T", "r", "qT", "qA")]
    return c | dict(e3=r*T*c["e1"], p3=r*T*c["p1"], t3=r*T*c["t2"],
        nu1=r*c["e1"]+T*tau*qt, nu2=r*c["e2"]+T*diffusion*qt,
        nu3=r*r*T*c["e1"]+tau*qa,
        ga1=r*c["t1"]-T*diffusion*qt, ga2=r*c["t2"]-T*diffusion*qt,
        ga3=r*r*T*c["t2"]-diffusion*qa)


def entropy(th, c):
    T, r, A, B = [th[a] for a in ("T", "r", "A", "B")]
    return dict(bulk=-c["p2"]-c["e1"]*A**2-T*c["nu3"]*B**2
        +A*(c["e2"]+c["p1"])+B*(c["p3"]+T*c["nu2"])
        -A*B*(c["e3"]+T*c["nu1"]),
        conduction=r*(c["t3"]-r*T*c["t1"])+r*T*c["ga1"]-c["ga3"],
        vector=c["ga2"]-c["ga1"]-r*(c["t2"]-c["t1"]))


def poly_from_matrix(matrix, normalization=1):
    return S.Poly(S.expand(normalization*matrix.det()), k).as_expr().subs(k**2, q).expand()


def hurwitz(poly):
    p = S.Poly(poly, s)
    n = p.degree()
    H = S.Matrix(n, n, lambda i, j: p.nth(n+i-2*j-1)
                 if 0 <= n+i-2*j-1 <= n else 0)
    return [S.factor(H[:j, :j].det()) for j in range(1, n+1)]


def root_record(poly, digits=80):
    poly = S.expand(poly)
    p = S.Poly(poly, s)
    entries = []
    for factor, multiplicity in S.factor_list(poly, s, extension=S.I)[1]:
        for root in S.Poly(factor, s).nroots(n=digits, maxsteps=1000):
            residual = abs(S.N(poly.subs(s, root), digits))
            scale = sum(abs(S.N(p.nth(j), digits))*abs(root)**j
                        for j in range(p.degree()+1))
            entries.append(dict(root=str(root), multiplicity=multiplicity,
                absolute_residual=str(residual),
                scaled_residual=str(S.N(residual/scale, 16)) if scale else "exact zero"))
    return dict(decimal_digits=digits, exact_polynomial=str(poly), degree=p.degree(),
                exact_coefficients_descending=[str(a) for a in p.all_coeffs()],
                roots=entries, scope="finite diagnostic, not universal proof")


def main():
    global RUN_OUTPUT
    RUN_OUTPUT = None
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="New subdirectory under generated/ (default: timestamped)")
    args = parser.parse_args()
    generated = (ROOT / "generated").resolve()
    out = (args.output or generated / datetime.now(timezone.utc).strftime("run-%Y%m%dT%H%M%S%fZ")).resolve()
    if generated not in out.parents:
        parser.error("output must be a new directory below this package's generated/ directory")
    out.mkdir(parents=True, exist_ok=False)
    RUN_OUTPUT = out
    checks.clear()
    requirements.clear()
    OUT = out
    inputs = json.loads((ROOT / "examples/inputs.json").read_text())

    T, w, x, delta = S.symbols("T0 w x Delta_J", positive=True)
    r, B = S.symbols("r B", real=True)
    e1, e2, p1, p2, t1, t2, eta = S.symbols("e1 e2 p1 p2 t1 t2 eta", real=True)
    Dq, tau, Dphys = S.symbols("Dq tau_q Dphys", nonnegative=True)
    c = dict(e1=e1, e2=e2, p1=p1, p2=p2, t1=t1, t2=t2, eta=eta)
    MN = neutral(w, x, c)
    PN = poly_from_matrix(MN, x)
    bulk = -p2-x*x*e1+x*(e2+p1)
    Gamma = 4*eta/3+bulk
    AL, BL = x*e1*t1, w*(x*e1+t1)
    CL = x*(e1*(4*eta/3-p2)+e2*(t2+p1)+t1*p1)
    DL, FL = x*BL+w*Gamma, x*t2*(p2-4*eta/3)
    target = AL*s**4+BL*s**3+(w*w+CL*q)*s*s+DL*q*s+x*w*w*q+FL*q*q
    check("neutral_original_determinant", PN-target)
    aa, bb, cc, dd, ff = S.symbols("A_L B_L C_L D_L F_L", real=True)
    abstract = aa*s**4+bb*s**3+(w*w+cc*q)*s*s+dd*q*s+x*w*w*q+ff*q*q
    minors = hurwitz(abstract)
    check("RH_delta2", minors[1]-(bb*w*w+(bb*cc-aa*dd)*q))
    check("RH_delta3", minors[2]-(bb*w*w*(dd-x*bb)*q+(dd*(bb*cc-aa*dd)-bb*bb*ff)*q*q))
    check("RH_delta4", minors[3]-(x*w*w*q+ff*q*q)*minors[2])
    cubic = x*e1*s**3+w*s*s+x*p1*q*s+x*w*q
    branch = PN.subs({e2:0,p2:4*eta/3})
    check("neutral_relaxation_times_cubic", branch-(t1*s+w)*cubic)
    check("neutral_relaxation_remainder", S.rem(branch,t1*s+w,s))
    ideal_remainder = S.rem(PN,s*s+x*q,s)
    check("ideal_sound_remainder_linear_s", S.Poly(ideal_remainder,s).nth(1)-w*Gamma*q)
    check("neutral_constant_q_obstruction", S.expand(PN.subs(s,0)).coeff(q,1)-x*w*w)

    # A regular thermodynamic chart derived from F=T^2 N and pressure identities.
    A = x-r*T*B
    E = w/(T*x)+T*delta*B*B/(w*x)
    N = r*E-delta*B/w
    F = T*T*N
    H = r*F+T*delta*A/w
    th = dict(T=T,w=w,n=r*w,r=r,E=E,F=F,N=N,H=H,A=A,B=B,
              qT=-delta*B/w,qA=T*delta*A/w,Delta_J=delta,Xi=T*delta*x/w,x=x)
    check("thermodynamic_Jacobian", E*H-F*N-delta)
    check("thermodynamic_Xi", th["qA"]-r*T*T*th["qT"]-th["Xi"])
    ch = uplift(th,c,Dq,tau)
    MC = charged(th,ch)
    fq = tau*s*s+s+Dq*q
    row = MC[2,:]-r*MC[0,:]-fq.subs(q,k*k)*S.Matrix([[th["qT"],th["qA"],0]])
    for j in range(3): check(f"charge_row_{j}",row[j])
    PC = S.factor(poly_from_matrix(MC))
    check("charged_original_determinant", PC+delta/w*fq*PN)
    check("charged_original_factor_remainder", S.rem(PC,fq,s))
    check("charged_original_full_remainder", S.rem(PC,-delta/w*fq*PN,s))
    ent = entropy(th,ch)
    check("charged_bulk",ent["bulk"]-(bulk-Dq*T*T*delta*B*B/w))
    check("charged_conduction",ent["conduction"]-Dq*th["Xi"])
    check("charged_vector",ent["vector"])
    check("auxiliary_bulk_shift", (Dq*T*T*delta*B*B/w).subs(Dq,Dphys*T/th["Xi"])-Dphys*T*T*B*B/x)

    v, gam, Om, K2 = S.symbols("v gamma Omega K2", real=True)
    gap = S.expand(abstract.subs({s:gam*s,q:-gam*gam*v*v*s*s},simultaneous=True)/(gam*gam*s*s))
    check("direct_neutral_lab_gap",gap-(gam*gam*(aa-cc*v*v+ff*v**4)*s*s+gam*(bb-dd*v*v)*s+w*w*(1-x*v*v)))
    R,Lh = S.symbols("R Lh",real=True)
    axis = S.re(abstract.subs({s:S.I*Om,q:K2},simultaneous=True))
    axis = axis.subs(Om**4,R*R*K2*K2).subs(Om**2,R*K2)
    check("imaginary_axis_identity",axis.subs(ff,aa*R*(cc/aa-R)-aa*Lh)-(w*w*(x-R)*K2-aa*Lh*K2*K2))
    ag,bg,cg,lq=S.symbols("a_g b_g c_g ell_q",positive=True)
    check("charged_gap_cubic_RH",(ag+lq*bg)*(bg+lq*cg)-lq*ag*cg-bg*(ag+lq*bg+lq*lq*cg))
    # Negative controls: these prevent the audit's invalid non-strict test.
    bad = hurwitz(s*s-1)
    check("negative_control_zero_minors",sum(a*a for a in bad))
    check("negative_control_unstable_root",(s*s-1).subs(s,1))
    check("zero_diffusion_degree_reduction",fq.subs({Dq:0,tau:0})-s)

    lam, amp = S.symbols("lambda Lambda", positive=True)
    d5 = 8*x*(1-x)+lam*(1+x)**2
    R5 = x+4*x*(1-x)**2/d5
    rho0 = (1+x)/2+(1-x)/(2*lam)
    check("F5_positive_R_margin",rho0-R5-(1-x)*(8*x*(1-x)+lam*(lam+1)*(1+x)**2)/(2*lam*d5))
    m6 = 1+6*x-3*x*x
    R6 = x+2*x*(1-x)**2/(amp*m6)
    sig6 = (3+x)/4-2*(amp-1)*x*(1-x)**2/(amp*(1+x)**2)
    phi6 = (amp-1)*x*(1-x)/(2*amp)
    Q6 = (amp-1)**2*(3*x-1)**2*m6*m6 + 2*(amp-1)*(1+x)*m6*(5*(1-x)+x*x*(19-3*x)) + (3-x)*(1+x)**3*(3+10*x-x*x)
    check("F6_positive_L_decomposition",R6*(sig6-R6)-phi6-x*(1-x)*Q6/(4*amp*amp*(1+x)**2*m6*m6))


    # Original coefficients are perturbed; no target determinant is substituted.
    fE, fP, fQ = S.symbols("f_E f_P f_Q", real=True)
    shifted = ch.copy()
    for one,three,fun in [("e1","e3",fE),("p1","p3",fP),("t2","t3",fQ)]:
        shifted[one] += T*th["qT"]*fun
        shifted[three] += th["qA"]*fun
    for current,stress in [("nu1","e1"),("nu3","e3"),("ga2","t2"),("ga3","t3")]:
        shifted[current] += r*(shifted[stress]-ch[stress])
    MS = charged(th,shifted)
    PS = S.factor(poly_from_matrix(MS))
    check("three_function_original_determinant",PS-PC)
    check("three_function_original_remainder",S.rem(PS,-delta/w*fq*PN,s))
    shifted_row = MS[2,:]-r*MS[0,:]-fq.subs(q,k*k)*S.Matrix([[th["qT"],th["qA"],0]])
    for j in range(3):check(f"three_function_charge_row_{j}",shifted_row[j])
    shifted_entropy=entropy(th,shifted)
    for key in ent:check("three_function_entropy_"+key,shifted_entropy[key]-ent[key])

    # Equal-transport boundary: F1--F3 lose a temporal degree when eta=theta1=0.
    ee, G = S.symbols("epsilon1 Gamma",positive=True)
    boundary_c = dict(e1=ee,e2=0,p1=x*ee+G/x,p2=0,t1=0,t2=0,eta=0)
    boundary_P=poly_from_matrix(neutral(w,x,boundary_c),x)
    boundary_target=w*(x*ee*s**3+w*s*s+(x*x*ee+G)*q*s+x*w*q)
    check("eta_zero_original_cubic",boundary_P-boundary_target)
    boundary_F3=boundary_c | {"t2":-(ee+x*ee+G/x)/2}
    check("eta_zero_F3_original_cubic",poly_from_matrix(neutral(w,x,boundary_F3),x)-boundary_target)
    check("Gamma_zero_F3_retained_gap",boundary_P.subs(G,0)-w*(x*ee*s+w)*(s*s+x*q))
    require("eta_zero_cubic_degree",S.Poly(boundary_P,s).degree()==3)
    check("zero_diffusion_retained_relaxation",fq.subs(Dq,0)-s*(1+tau*s))
    kZ,kP=S.symbols("k_z k_perp",real=True)
    boost_args={s:gam*(s+S.I*v*kZ),q:kP*kP+gam*gam*(kZ-S.I*v*s)**2}
    full_ch_gap=S.cancel(PC.subs({s:gam*s,q:-gam*gam*v*v*s*s},simultaneous=True)/(gam**3*s**3))
    expected_gap=-delta/w*(1+gam*(tau-Dq*v*v)*s)*gap.subs({aa:AL,bb:BL,cc:CL,dd:DL,ff:FL})
    check("original_charged_lab_gap_product",full_ch_gap-expected_gap)
    check("original_charged_boosted_factorization",PC.subs(boost_args,simultaneous=True)+delta/w*fq.subs(boost_args,simultaneous=True)*PN.subs(boost_args,simultaneous=True))

    PT=t1*s*s+w*s+eta*q
    full_neutral=S.expand(PT**2*PN)
    full_charged=S.expand(PT**2*PC)
    def degrees(polynomial):
        poly=S.Poly(polynomial,s,q)
        return dict(frequency=poly.degree(s),total_derivative=max(a+2*b for (a,b),coef in poly.terms()))
    degree_records={"neutral_nondegenerate":degrees(full_neutral),"charged_nondegenerate":degrees(full_charged)}
    for name,degree in [("neutral_nondegenerate",8),("charged_nondegenerate",10)]:
        require(name+"_frequency_degree",degree_records[name]["frequency"]==degree)
        require(name+"_total_derivative_degree",degree_records[name]["total_derivative"]==degree)
    divisions={}
    for name,original,divisor,expected,domain in [
        ("neutral_relaxation",branch,t1*s+w,cubic,"theta1 != 0 for this degree-one division; the polynomial difference also covers theta1=0"),
        ("charged_telegrapher",PC,fq,-delta/w*PN,"tau_q != 0 for this degree-two division; zero-transport reductions checked separately"),
        ("charged_full",PC,-delta/w*fq*PN,S.S.One,"nonzero leading coefficient for this degree-six division; undivided identity holds on reduced branches")]:
        quotient,remainder=S.div(original,divisor,s)
        check(name+"_quotient",quotient-expected)
        check(name+"_division_remainder",remainder)
        divisions[name]=dict(original=original,divisor=divisor,quotient=S.factor(quotient),remainder=S.factor(remainder),division_domain=domain)
    y,cv,ct=S.symbols("y c cos_phi",real=True)
    speed=(cv-v*ct)**2-y*((ct-v*cv)**2+(1-v*v)*(1-ct*ct))
    expected_speed=(1-y*v*v)*cv*cv-2*v*(1-y)*ct*cv+v*v*ct*ct-y*(1-v*v+v*v*ct*ct)
    check("all_angle_characteristic_equation",speed-expected_speed)
    check("luminal_characteristic_endpoint",speed.subs(y,1)-(1-v*v)*(cv*cv-1))
    check("zero_speed_characteristic_endpoint",speed.subs(y,0)-(cv-v*ct)**2)
    check("luminal_neutral_leading",(aa-cc*v*v+ff*v**4).subs({cc:aa,ff:0})-aa*(1-v*v))
    examples=[]
    tt,mm=S.symbols("T mu",real=True)
    for spec in inputs["cases"]:
        name=spec["name"]
        ell,ee,zz,dc = [S.Rational(spec[key]) for key in ("ell","eta","zeta","Dphys")]
        for key,value in [("eta",ee),("zeta",zz),("Dphys",dc)]:
            require(name+"_physical_"+key,value>=0)
        T0,mu0=[S.Rational(inputs[key]) for key in ("T0","mu0")]
        require("example_temperature_normalization",T0==1)
        pressure=tt**4+tt*tt*mm*mm+ell*tt*tt
        energy=-pressure+tt*S.diff(pressure,tt)+mm*S.diff(pressure,mm)
        density=S.diff(pressure,mm)
        ev=lambda a:S.factor(a.subs({tt:T0,mm:mu0}))
        ww,nn=ev(energy+pressure),ev(density)
        rr=nn/ww
        der=lambda h:(ev(S.diff(h,tt)+mm/tt*S.diff(h,mm)),ev(tt*S.diff(h,mm)))
        et,ea=der(energy);nt,na=der(density)
        de=et*na-ea*nt;qt=nt-rr*et;qa=na-rr*ea
        aval=ww*qa/de;bval=-ww*qt/de;xx=aval+rr*bval
        tv=dict(T=S.S.One,w=ww,n=nn,r=rr,E=et,F=ea,N=nt,H=na,A=aval,B=bval,qT=qt,qA=qa,Delta_J=de,Xi=qa-rr*qt,x=xx)
        nmu=ev(S.diff(density,mm))
        domain_margins=dict(T=S.S.One,w=ww,Delta_J=de,x=xx,one_minus_x=1-xx,
            E=et,n_mu=nmu,compound=aval+nmu*bval*bval/ww-rr*bval,
            charge_fluctuation=nmu-nn*nn/(ww*xx))
        for key,value in domain_margins.items():
            require(name+"_domain_"+key, value>0 if key in ("T","w","Delta_J","x","one_minus_x") else value>=0)
        GG=4*ee/3+zz+dc*bval*bval/xx
        amp=S.Rational(inputs["Lambda"]);beta=S.Rational(inputs["beta"]);alphaq=S.Rational(inputs["alpha_q"]);chi=beta*(3*xx-1)**2/(1+(3*xx-1)**2)
        require("example_amplitude_range",S.And(amp>1,amp<=2))
        require("example_deformation_range",S.And(beta>=0,beta<=1))
        require("example_charge_speed_range",alphaq>=1)
        sig0=(3+xx)/4-2*(amp-1)*xx*(1-xx)**2/(amp*(1+xx)**2)
        tv1=amp*GG*(1+xx)**2/(2*xx*(1-xx)**2)
        cv=dict(e1=2*amp*GG/(xx*(1-xx)),e2=amp*GG*(1+xx)/(2*xx*(1-xx)),
          p1=amp*GG*(1+xx)/(2*xx*(1-xx)),p2=4*ee/3+(amp-1)*GG,
          t1=tv1,t2=tv1*(1+4*chi*(1-sig0)/(1+xx)),eta=ee)
        dq=dc/tv["Xi"];cv=uplift(tv,cv,dq,alphaq*dq)
        pp=S.factor(poly_from_matrix(charged(tv,cv)))
        pn=S.factor(poly_from_matrix(neutral(ww,xx,cv),xx))
        check(name+"_original_remainder",S.rem(pp,-de/ww*(alphaq*dq*s*s+s+dq*q)*pn,s))
        es=entropy(tv,cv)
        for key,expected in [("bulk",zz),("conduction",dc),("vector",0)]:
            check(name+"_entropy_"+key,es[key]-expected)
        # Rational boost and oblique lab wavevector give gamma=5/3 exactly.
        vb=S.Rational(inputs["v"]);gb=1/S.sqrt(1-vb*vb);kz=S.Rational(inputs["kz"]);kp=S.Rational(inputs["kperp"])
        require("example_finite_boost",abs(vb)<1)
        pb=S.expand(pp.subs({s:gb*(s+S.I*vb*kz),q:kp*kp+gb*gb*(kz-S.I*vb*s)**2},simultaneous=True))
        pg=S.cancel(pp.subs({s:gb*s,q:-gb*gb*vb*vb*s*s},simultaneous=True)/(gb**3*s**3))
        record=dict(name=name,pressure=pressure,ell=ell,T0=T0,mu0=mu0,
          eta=ee,zeta=zz,Dphys=dc,amplitude=amp,beta=beta,alpha_q=alphaq,
          thermodynamics=tv,coefficients=cv,original_matrix=charged(tv,cv),
          domain_margins=domain_margins,
          original_polynomial=pp,neutral_polynomial=pn,boost=vb,kz=kz,kperp=kp,
          rest=root_record(pp.subs(q,kz*kz+kp*kp)),boosted=root_record(pb),
          gaps=root_record(pg) if S.Poly(pg,s).degree()>0 else {"exact_polynomial":str(pg),"degree":0})
        if name=="conformal_benchmark":
            for key,val in dict(e1=24*ee,e2=8*ee,p1=8*ee,p2=8*ee/3,t1=16*ee,t2=16*ee).items():
                check("benchmark_"+key,cv[key]-val)
            for j in (1,2,3):check(f"benchmark_conformal_e{j}",cv[f"e{j}"]-3*cv[f"p{j}"])
            check("benchmark_conformal_nu",cv["nu1"]-3*cv["nu2"])
            check("benchmark_conformal_ga",cv["ga1"]-cv["ga2"])
            y=S.symbols("y")
            principal=S.Poly(pn,s,q)
            apr=principal.coeff_monomial(s**4)
            cpr=principal.coeff_monomial(s*s*q)
            fpr=principal.coeff_monomial(q*q)
            check("benchmark_sound_speeds",y*y-cpr/apr*y+fpr/apr-(y-S.Rational(1,12))*(y-S.Rational(2,3)))
            check("benchmark_shear_speed",ee/cv["t1"]-S.Rational(1,16))
            check("benchmark_charge_speed",dq/(alphaq*dq)-S.Rational(1,2))
        if name=="conformal_zero_transport":
            check("zero_transport_original_Euler",pp+de*ww*s*(s*s+xx*q))
            require("zero_transport_degree",S.Poly(pp,s).degree()==3)
        full_example=(cv["t1"]*s*s+ww*s+ee*q)**2*pp
        record["full_system_degrees"]=degrees(full_example)
        degree_records[name]=record["full_system_degrees"]
        if name=="conformal_zero_transport":
            require("Euler_full_degree_frequency",record["full_system_degrees"]["frequency"]==5)
            require("Euler_full_degree_total",record["full_system_degrees"]["total_derivative"]==5)
        examples.append(record)

    source=ROOT/"Paper/BDNKFrames.tex"
    labels={}
    for line_number,line in enumerate(source.read_text().splitlines(),1):
        for label in re.findall(r"\\label\{([^}]+)\}",line):labels[label]=line_number
    (OUT/"paper_labels.json").write_text(json.dumps(labels,indent=2)+"\n")
    result=dict(scope="Selected exact identities plus three rational diagnostic examples; no new-system certificate",
        checks=checks,exact_requirements=requirements,degree_records=degree_records,division_certificates=divisions,
        shifted_original_matrix=MS,shifted_original_polynomial=PS,
        original_charged_lab_gap=full_ch_gap,eta_zero_original_cubic=boundary_P,
        neutral_matrix=MN,neutral_polynomial=PN,charged_matrix=MC,
        charged_polynomial=PC,thermodynamic_chart=th,ideal_sound_remainder=ideal_remainder,
        examples=examples,python=sys.version,sympy=S.__version__,platform=platform.platform(),
        mpmath=mpmath.__version__,inputs_sha256=hashlib.sha256((ROOT/"examples/inputs.json").read_bytes()).hexdigest(),
        script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        manuscript_sha256=hashlib.sha256(source.read_bytes()).hexdigest())
    (OUT/"verification.json").write_text(json.dumps(encode(result),indent=2)+"\n")
    messages=[f"PASS: {len(checks)} exact residual checks and {len(requirements)} exact requirements.",
        "Saved three rational examples with 80-digit roots and absolute/scaled residuals.",
        "Numerical samples are diagnostics; analytic universal obligations remain separately scoped."]
    (OUT/"run.log").write_text("\n".join(messages)+"\n")
    print("\n".join(messages))
    print("Output:",OUT)



if __name__=="__main__":
    try:
        main()
    except Exception as error:
        if RUN_OUTPUT is not None:
            (RUN_OUTPUT/"failure.json").write_text(json.dumps(dict(
                status="failed",error=repr(error),checks=checks,exact_requirements=requirements,
                script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                inputs=(ROOT/"examples/inputs.json").read_text(),
                traceback=traceback.format_exc()),indent=2)+"\n")
            (RUN_OUTPUT/"run.log").write_text(traceback.format_exc())
        raise
