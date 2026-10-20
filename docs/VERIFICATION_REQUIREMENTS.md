# Verification requirements and known false shortcuts

Read the [protocol](RESEARCH_PROTOCOL.md) for the full calculations. This file is a standalone verification contract; it requires no earlier project history.

| Claim | Required evidence | Insufficient substitute |
|---|---|---|
| Correct physical transport | Original entropy divergence, invariant map, prescribed-input residuals after the final coefficient assignment | A target polynomial or an auxiliary bulk labeled physical |
| Factorization | Original matrix determinant difference; exact quotient and remainder with normalization; branch and denominator ledger | Factoring a constructed target or matching numerical roots |
| Rest spectral stability | Analytic all-real-momentum sign/root count; zero-momentum conservation and gaps | A finite scan or only large/small momentum |
| Boost spectral stability | Original laboratory gaps; complex root criterion or no-crossing plus no-infinity proof on every finite boost interval | Rest stability plus covariance; boosting a rest k=0 root |
| Causal characteristics | Full physical/constraint principal system, all directions, real speeds <=1, degree audit, degeneracies | Only longitudinal modes, symmetry axes or one branch's asymptotic slope |
| Nonnegative-transport domain | Substitution into original matrices on each boundary and intersection; new degree, gaps and proof | Dividing by vanished coefficients then taking ratios |
| Finite symmetry limit | Bounded functions and absolute symmetry residuals along every allowed approach | One exact conformal point or divergent ratio limit |
| Stronger PDE result | Compatible constraints, evolution reduction, eigenvectors/estimates and theorem hypotheses or direct proof | Spectral roots alone |

Normalize real polynomials with a proved positive leading coefficient before strict Routh–Hurwitz tests. `s^2-1` has all ordinary Hurwitz minors zero yet a positive root. Nonnegative minors alone are not a closed-left-half-plane criterion. For a fixed marginal polynomial one route is strict RH of `p(s+epsilon)` for all sufficiently small positive epsilon, determined by exact first nonzero epsilon coefficients. Check Jordan structure separately for bounded evolution.

For a complex polynomial use a justified complex criterion or real RH on `p(s)*coefficient_conjugate(p)(s)`. This product has the original roots and their conjugates. It is not a direct Bilharz construction. Squared absolute values of ordinary complex Hurwitz minors cannot supply signs. A condition number cannot supply a determinant sign either.

Every zero remainder check must start with the original matrix and save the quotient: a zero remainder can coexist with a wrong claimed normalization or missing multiplicity. Reject a candidate with a nonzero entropy residual even if its determinant factorization succeeds. Sufficient positivity certificates may fail inconclusively; distinguish that from violating a necessary condition or finding an unstable root.

The supplied verifier checks selected generic identities, polynomial degrees, three-function determinant/entropy preservation, and three exact rational examples. It does not automatically rederive the tensor-basis completeness, entropy-current derivation, all six family sign proofs, the stronger local quadratic-factor obstruction, all nonlinear theorem hypotheses, or a new system's constraints. These remain human-readable conditional arguments or explicitly open obligations in the ledger.

Preserve rejected candidates. Never change tolerances until a check passes. Record precision, inputs, source hashes, solver, output and any failure. Establish universal claims analytically; finite diagnostics remain finite diagnostics.
