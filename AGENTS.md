# Instructions for an AI using this package

Read `README.md`, `docs/CONVENTIONS.md`, `docs/VERIFICATION_REQUIREMENTS.md`, `docs/RESEARCH_PROTOCOL.md`, `docs/BOUNDARY_ANALYSIS.md`, and `reference_results/proof_ledger.json`. Read the frozen `Paper/BDNKFrames.tex`, including its appendix, before attributing a construction or theorem to it. `docs/PAPER_SOURCE.html` provides equation-label links. Verify `MANIFEST.json` with `scripts/check_package.py`.

Treat the manuscript as a source to examine. An exact algebra check, a conditional analytic proof, a finite diagnostic, and an unresolved claim are different evidence. Keep those distinctions in the ledger. The supplied examples certify no new physical system.

## Research contract

1. Specify fields, conservation laws, constraints, sources, symmetries, thermodynamics, and allowed states. Distinguish physical transport from adjustable frame functions. Do not change the problem to rescue a failed ansatz.
2. Derive entropy and its invariant transport combinations, then assemble the original conservation matrix. Prove its sector decomposition; analyze shear or another genuinely autonomous simpler sector first. Shear factors out of the full fluid determinant, leaving the longitudinal block.
3. Compare longitudinal degree partitions and root allocations. Test local coefficient ansätze against the original polynomial and entropy. A telegrapher factor is a possible outcome, not a requirement. Retain an unsplit polynomial or matrix block if necessary.
4. Derive coefficients and analytic sign/regularity certificates. Match every prescribed transport. In the benchmark, eta, zeta and physical script-D are free nonnegative inputs. The charged auxiliary bulk is not physical zeta. No division by B or qT without a removable-singularity proof on every permitted approach.
5. Recheck the original determinant and all entropy identities after every coefficient change. Save exact difference, quotient and remainder, leading signs, all assumptions, and all excluded branches.
6. Prove stability for every real momentum including zero and every finite boost. Derive laboratory gaps from the original boosted determinant. Covariance and rest stability do not suffice. Check all directions, constraints, degree changes, repeated roots, marginal modes and causal saturation. Keep the bound <=1, including its endpoints.
7. Separate spectral root location from bounded evolution, characteristic/cone causality, strong hyperbolicity, and nonlinear well-posedness. Do not use a cited theorem in place of the direct spectral calculations requested by this protocol.

Use the Fourier convention `exp(-i omega t+i k.x)`, growth rate `s=-i omega`, so `omega=i s` and stability means `Re(s)<=0`. The paper denotes this rate by varsigma and uses s for entropy density. Use T0 and mu0 for equilibria. See the notation dictionary before writing code.

## Calculations and evidence

Use exact rational/algebraic inputs. Increasing the precision of a machine float does not restore lost digits. Save polynomial coefficients, precision, roots, multiplicities and absolute/scaled residuals. Numerical scans diagnose; they do not prove universal quantifiers.

Do not replace strict Hurwitz minors by nonnegative minors: `s^2-1` is a counterexample. For complex coefficients, RH of the coefficient-conjugate product is valid for strict root location; call it by that name. Realifying ordinary complex Hurwitz matrices is not a Bilharz criterion. A condition number is not a sign test.

Use the four ledger statuses `established_identity`, `conditional_result`, `conjecture`, `unresolved_gap`. Record failed ansätze separately with exact reasons and scope. Do not assert general nonexistence from a single failed factorization. Every claimed universal result needs explicit quantifiers, domain, dependency list, boundary coverage and a written analytic argument.

## Workspace and execution

Keep `Paper/`, `reference_results/`, and the distributed protocol unchanged. Create versioned work under `generated/studies/` using `scripts/new_study.py`, or in another separately authorized research directory. Never delete existing study output to force a clean run. New source versions receive new hashes and ledgers.

Run the commands in README. They use only this package and its pinned dependencies. No project history, web account, Wolfram installation or parent-repository imports are required. Before returning a candidate family, provide its original matrices, entropy calculation, coefficient map, exact factor checks, analytic rest/boost proofs, directional characteristics, boundaries, examples and proof ledger. If a proof is missing, identify the exact unresolved obligation and retain the candidate's actual scope.
