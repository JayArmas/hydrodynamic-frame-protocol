# AI research protocol for stable and causal hydrodynamic frames

Supplementary package version 1.0.0, 20 October 2026. This protocol extracts a construction method from the final supplied [BDNK manuscript](../Paper/BDNKFrames.tex) and its appendix. Its purpose is to guide actual derivations in a new system, before selecting magnetohydrodynamics, superfluidity, multiple charges or anisotropy as an application. No new system or frame family is certified here. The manuscripts are source material, not axioms.

The sequence is: specify the physics; derive entropy and the original equations; decompose sectors and analyze shear first; investigate possible longitudinal factorizations; solve the resulting coefficient inequalities; verify the original system, boosts and boundaries; publish a scoped proof ledger. A telegrapher factor is one possible outcome of the factorization search. A coupled polynomial, or a matrix block that does not split into scalar factors, is also a valid outcome.

## Structure and map to the paper

The labels below identify the current source more reliably than equation numbers, which change with editing. The accompanying evidence records its SHA256 hash and a complete label-to-line map. References to manuscript F1–F6 mean its current catalogue, not historical families with reused numbers. Family IDs in this package are `paper-F1` through `paper-F6`, tied to the frozen manuscript hash; they are not identifiers for any external archive.

| Stage | Calculation and deliverable | Paper equations or arguments |
|---|---|---|
| 1 | Fix fields, equations, physical inputs, symmetries and domain | [eq:stress](PAPER_SOURCE.html#eq:stress), [eq:current](PAPER_SOURCE.html#eq:current), [eq:scalars](PAPER_SOURCE.html#eq:scalars), [eq:vectors](PAPER_SOURCE.html#eq:vectors), [eq:domain](PAPER_SOURCE.html#eq:domain), [app:assumptions](PAPER_SOURCE.html#app:assumptions) |
| 2 | Derive entropy production and transport invariants | [app:eq:neutral-entropy-divergence](PAPER_SOURCE.html#app:eq:neutral-entropy-divergence), [app:eq:neutral-entropy-final](PAPER_SOURCE.html#app:eq:neutral-entropy-final), [eq:entropy](PAPER_SOURCE.html#eq:entropy), [eq:matching](PAPER_SOURCE.html#eq:matching) |
| 3 | Assemble original matrices, decompose sectors and solve shear first | [eq:strategy-full-polynomial](PAPER_SOURCE.html#eq:strategy-full-polynomial), [eq:strategy-shear-polynomial](PAPER_SOURCE.html#eq:strategy-shear-polynomial), [app:eq:neutral-matrix](PAPER_SOURCE.html#app:eq:neutral-matrix), [app:original-charged-matrix](PAPER_SOURCE.html#app:original-charged-matrix) |
| 4 | Classify and test candidate longitudinal factorizations | [eq:neutral-sound-polynomial](PAPER_SOURCE.html#eq:neutral-sound-polynomial), [eq:relax-factor](PAPER_SOURCE.html#eq:relax-factor), [eq:strategy-factorization](PAPER_SOURCE.html#eq:strategy-factorization), [fn:neutral-quadratic-obstruction](PAPER_SOURCE.html#fn:neutral-quadratic-obstruction) |
| 5 | Reduce inequalities and construct coefficient branches and limits | [eq:invariants](PAPER_SOURCE.html#eq:invariants), [eq:rh](PAPER_SOURCE.html#eq:rh), [eq:certificate](PAPER_SOURCE.html#eq:certificate), [eq:luminal-design](PAPER_SOURCE.html#eq:luminal-design), [eq:AG](PAPER_SOURCE.html#eq:AG), [eq:AN](PAPER_SOURCE.html#eq:AN), [app:eq:charged-AN-positive-Q](PAPER_SOURCE.html#app:eq:charged-AN-positive-Q) |
| 6 | Seek autonomous fluctuations and derive coefficient maps | [app:eq:charged-uplift-row](PAPER_SOURCE.html#app:eq:charged-uplift-row), [eq:uplift-stress](PAPER_SOURCE.html#eq:uplift-stress), [eq:uplift-current](PAPER_SOURCE.html#eq:uplift-current), [app:eq:charged-uplift-bulk](PAPER_SOURCE.html#app:eq:charged-uplift-bulk), [app:eq:hierarchy-five](PAPER_SOURCE.html#app:eq:hierarchy-five) |
| 7 | Recheck entropy, original determinants, conservation roots and all real rest momenta | [app:eq:neutral-design-unreduced](PAPER_SOURCE.html#app:eq:neutral-design-unreduced), [app:eq:neutral-design-causal](PAPER_SOURCE.html#app:eq:neutral-design-causal), [eq:factorization](PAPER_SOURCE.html#eq:factorization), [app:eq:hierarchy-isospectral](PAPER_SOURCE.html#app:eq:hierarchy-isospectral) |
| 8 | Prove arbitrary-boost stability, laboratory gaps and directional characteristics | [app:eq:neutral-boost](PAPER_SOURCE.html#app:eq:neutral-boost), [app:eq:neutral-gaps](PAPER_SOURCE.html#app:eq:neutral-gaps), [app:eq:neutral-axis-exclusion](PAPER_SOURCE.html#app:eq:neutral-axis-exclusion), [app:eq:neutral-speed-quadratic](PAPER_SOURCE.html#app:eq:neutral-speed-quadratic), [app:eq:charged-uplift-gaps](PAPER_SOURCE.html#app:eq:charged-uplift-gaps) |
| 9 | Resolve marginal modes, degree changes and the scope of nonlinear claims | [fn:F3-large-k-damping](PAPER_SOURCE.html#fn:F3-large-k-damping), [fn:neutral-zero-transport](PAPER_SOURCE.html#fn:neutral-zero-transport), [fn:charged-zero-transport](PAPER_SOURCE.html#fn:charged-zero-transport), [fn:independent-charge-relaxation](PAPER_SOURCE.html#fn:independent-charge-relaxation), [sec:nonlinear-discussion](PAPER_SOURCE.html#sec:nonlinear-discussion) |
| 10 | Save reproducible derivations, counterexamples and a claim ledger | All preceding calculations, with the requirements of [AGENTS.md](../AGENTS.md) and [the verification contract](VERIFICATION_REQUIREMENTS.md) |

Stages 4–6 form an iterative search. Stage 3 supplies shear bounds that constrain this search. A failure in verification returns to the relevant construction stage, preserving the failed candidate and its evidence.

## Conventions and critical reading rules

Use signature \((-+++ )\), Fourier dependence \(e^{-i\omega t+i\mathbf k\cdot\mathbf x}\), and growth rate \(s=-i\omega\), so \(\omega=is\) and stability means \(\Re s\leq0\). The paper uses \(\varsigma\) for this growth rate and \(s\) for entropy density. This protocol uses \(s_{\rm ent}\) for entropy density. Write equilibrium quantities at \((T_0,\mu_0)\); suppress the subscript only after declaring evaluation there.

Keep distinct the equilibrium energy \(\epsilon\), frame coefficients \(\varepsilon_i\), EoS perturbation \(\ell\), conductivity \(\mathcal D\), diffusivity \(D_q\), susceptibility determinant \(D_J=\epsilon_Tn_\mu-\epsilon_\mu n_T\), and \(\Delta_J=T_0D_J\). Code names `n0`, `w0`, `Delta`, `vs2`, `Dphys` correspond to \(n,w,\Delta_J,x,\mathcal D\). All formulas below are pointwise in equilibrium data unless a function-space statement is explicitly supplied.

Apply these qualifications when extracting the method:

- Nonnegative transport does not imply \(\Gamma>0\). The divided quartic analysis needs \(\Gamma,A_L,B_L>0\); zero inputs belong to Stage 9. The final manuscript distinguishes this positive-transport branch from its zero-transport footnotes.
- The neutral linear-times-cubic split requires both \(\varepsilon_2=0\) and \(\pi_2=4\eta/3\). Setting \(\varepsilon_2=0\) alone in the unrestricted matrix is insufficient.
- The paper explains that general sextic inequalities are harder to solve explicitly; this motivates a simplifying search, not an impossibility result. Other systems may permit different reductions.
- The quadratic-factor obstruction in the final manuscript is stated for a particular local quadratic ansatz, finite conformal matching and positive limiting shear. This package does not independently establish that stronger classification. Do not use it to prune every quadratic ansatz; the narrower two-standard-telegrapher obstruction below is checked exactly.
- Completeness of the three-function charged freedom is restricted to the fixed charge-row identity. It does not classify all determinants with a quadratic factor. Equal determinants do not establish equal eigenspaces.
- The current charged map does not require \(A\geq0\). Historical diagnostics containing that gate must not silently narrow its domain. Conversely, its strict susceptibility domain does not cover \(\Delta_J=0\).
- Nonlinear literature remarks in the Discussion are starting points for a separate hypothesis audit. Neither a thermodynamic-frame equality nor linear spectral factorization establishes applicability of a nonlinear theorem.

## Stage 1 Specify the physical problem

**Required inputs.** Supply spacetime dimension and background geometry; dynamical fields; external versus dynamical sources; conservation laws; algebraic, differential and gauge constraints; derivative order; parity and time-reversal assumptions; equilibrium states; constitutive regularity; EoS; physical transport; and requested symmetry limits. Explicitly state whether the task concerns the exact evolution equations obtained from a truncated constitutive law or only their long-wavelength expansion.

**Calculation.** Choose independent fields \(U^A\), resolve algebraic constraints such as \(u^2=-1\) in a regular chart, and write every original equation \(\mathcal E_a[U]=0\). Build a complete independent first-derivative tensor basis consistent with the declared symmetries. Keep constraint evolution equations visible. Identify frame changes \(U^A\mapsto U^A+\delta U^A_{(1)}\) and compute how they act on the constitutive coefficients at the retained order. A change equivalent in the gradient expansion need not preserve the exact truncated PDE spectrum.

Specify which homogeneous equilibria admit the Fourier analysis. For an inhomogeneous background, a frozen-coefficient symbol is a local diagnostic; it is not a global spectral-stability proof for the variable-coefficient evolution.

For the paper's single-charge example the fields are \((T,\alpha,u^i)\), \(\alpha=\mu/T\); the equations are stress and charge conservation; there is no external electromagnetic field. Compute \(n=p_\mu\), \(s_{\rm ent}=p_T\), \(\epsilon=-p+Tp_T+\mu p_\mu\), \(w=\epsilon+p\), susceptibilities, and \(x\) from the EoS. Do not independently assign inconsistent thermodynamic derivatives. The working domain is \(T,w,\Delta_J>0\), \(0<x<1\), together with the stated fluctuation inequalities. Its regularity and ideal-sound restrictions are extra domain assumptions, not consequences of entropy production alone.

Partition coefficients into prescribed physical functions, adjustable frame functions, and any additional physical nondissipative functions. In a coupled system, prescribed dissipative transport can be a positive semidefinite matrix. Its off-diagonal entries need not individually be nonnegative; nondissipative antisymmetric entries do not contribute to the entropy quadratic form. Impose reciprocity only under the symmetries that justify it.

**Expected outputs.** A problem specification, independent tensor basis, coefficient dictionary with units and derivative orders, a frame-transformation map, and an explicit admissible state/transport domain. State whether bounds are pointwise or uniform and whether zero or luminal characteristic speeds are permitted. Here physical speeds \(\leq1\) are permitted; a request for nonzero strictly subluminal speeds is a separate strengthened target.

**Proceed when.** Every physical input is distinguished from a frame parameter, the equilibrium satisfies the original equations and constraints, and every coordinate inversion has a declared domain.

**Failure modes and alternatives.** If susceptibilities are singular, change variables or analyze that stratum separately. If a field or source choice changes the system, record it as a different problem. A prohibited transport value or changed EoS cannot be used to rescue an ansatz.

**Save.** `problem_spec`, exact EoS and derivative expressions, tensor basis, units, constraint list, assumption list, and source provenance. Record all domain exclusions explicitly.

## Stage 2 Derive entropy and invariant transport

**Required inputs.** The original constitutive relations, thermodynamic differential identities, ideal equations, and the allowed entropy-current terms.

**Calculation.** Derive the entropy divergence before selecting a frame. For the paper's neutral and charged canonical currents,

\[
S^\mu=\frac{p u^\mu-u_\nu T^{\mu\nu}-\mu J^\mu}{T},\qquad
\nabla_\mu S^\mu=-T_{(1)}^{\mu\nu}\nabla_\mu(u_\nu/T)
-J_{(1)}^\mu\nabla_\mu\alpha.
\]

Omit the charge term in the neutral system. Derivatives of coefficient functions cancel in this identity before the constitutive expansion. Check the cancellation rather than treating coefficients as constants in a nonlinear entropy derivation. If a new system requires noncanonical entropy-current terms, include and determine them.

Expand through the controlled quadratic derivative order. Reduce with the ideal equations only to the accuracy that makes the discarded terms cubic. Express the result in a basis of independent dissipative forces \(X_I\):

\[
T\nabla_\mu S^\mu=X_I\mathsf L_{IJ}X_J+O(\partial^3).
\]

Compute the symmetric part of \(\mathsf L\), its positivity conditions, and the frame-invariant coefficient combinations. Verify their invariance under the Stage 1 transformations. Solve the equalities matching these combinations to the prescribed physical transport. A vanishing diagonal with a surviving mixed quadratic term is a positivity obstruction; in the paper it forces the vector identity rather than equality of the two vector frame coefficients.

The paper supplies the following benchmark residuals, all of which must vanish after each candidate modification:

\[
\begin{aligned}
Z&=-\pi_2-\varepsilon_1A^2-T\nu_3B^2+A(\varepsilon_2+\pi_1)
+B(\pi_3+T\nu_2)-AB(\varepsilon_3+T\nu_1)-\zeta,\\
C&=r(\theta_3-rT\theta_1)+rT\gamma_1-\gamma_3-\mathcal D T,\\
V&=\gamma_2-\gamma_1-r(\theta_2-\theta_1),\qquad r=n/w.
\end{aligned}
\]

For neutral seeds the scalar equation is
\(\zeta_*=-\pi_2-x^2\varepsilon_1+x(\varepsilon_2+\pi_1)\).
Here \(\pi_2\) is a frame coefficient, not physical bulk viscosity. In the charged construction \(\zeta_*\) is an auxiliary seed input, not the physical charged \(\zeta\).

**Expected outputs.** Off-shell quadratic contraction, ideal on-shell reduction, invariant transport map, positivity conditions and an entropy-compatible coefficient parametrization.

**Proceed when.** Matching is exact, the prescribed transport remains free throughout its stated domain, and positivity holds at the retained order. Off-shell positivity for arbitrary independent time derivatives is a different requirement and must not be imposed inadvertently.

**Failure modes and alternatives.** A matching equation may be redundant because of thermodynamic identities. Compute its symbolic rank before division; a numerical near-zero slope is not an adjustable parameter. Choose a different elimination variable or branch, or enlarge the entropy-current ansatz if allowed by the original problem. Do not manufacture a new physical transport value.

**Save.** Both entropy expressions, ideal substitutions, the transformation/invariance calculation, all matching residuals and rank/denominator conditions, including failed solutions.

## Stage 3 Derive sector decomposition and analyze shear first

**Required inputs.** The entropy-compatible but otherwise general constitutive system and a uniform admissible background.

**Calculation.** Linearize the original conservation and constraint equations in independent amplitudes. Retain signs, factors of \(i\), field normalizations and equation ordering. Freeze coefficients only after linearization about the uniform state. Store the matrix \(M_{\rm orig}(s,\mathbf k)\) before making a simplifying frame ansatz.

Use the residual symmetry of the background to decompose this matrix. In the isotropic fluid, the two transverse velocity polarizations separate naturally from the longitudinal block:

\[
\det M_{\rm full}\propto P_T^2P_L,\qquad
P_T=\theta_1s^2+ws+\eta q,\qquad q=|\mathbf k|^2.
\]

Thus shear factors out of the full dispersion determinant, leaving the longitudinal polynomial to analyze. It is not a factor of the longitudinal polynomial itself. Derive the block transformation and its nonzero determinant; a coordinate choice \(\mathbf k\parallel\hat z\) is justified here by isotropy.

Analyze this simpler sector first. For \(w,\eta,\theta_1>0\), its rest roots are damped for \(q>0\), its zero-momentum roots are \(0,-w/\theta_1\), and its squared speed is \(y_T=\eta/\theta_1\). The design \(\theta_1=\alpha_T\eta\), \(\alpha_T\geq1\), solves shear stability and causal-speed conditions. Carry this bound into the longitudinal search because \(\theta_1\) occurs there too. Stage 8 supplies the direct boost proof; Stage 9 handles \(\eta=0\) and degree changes.

In a less symmetric system, first determine whether an autonomous shear block exists at general direction. A background magnetic field, superflow or anisotropy can mix polarizations. Analyze any independently established simpler block first, retain coupled transverse blocks when necessary, and do not extrapolate an axial-direction factorization to oblique propagation.

For the remaining block, compute its exact determinant or physical matrix pencil on the constraint-compatible subspace. At \(\mathbf k=0\), identify conservation zero modes from the original matrix and extract the relaxation polynomial. Count temporal degree, constraints, physical modes and multiplicities. Neutral longitudinal flow has two conservation zeros and, on the regular quartic branch, two gaps; the charged longitudinal sextic has three and three. The full neutral/charged systems have additional transverse conservation modes.

Compute the principal matrix by derivative order in the original equations. For a uniform-order system this means scaling \((s,\mathbf k)\mapsto\lambda(s,\mathbf k)\) and extracting the highest homogeneous part. If different equations have different orders, establish a consistent weighted principal system or a justified first-order reduction first. Do not guess the physical principal symbol from the highest power of one determinant variable. Also compare frequency degree with total derivative degree of the full local determinant, retaining every sector. In the nondegenerate paper branches, `P_T^2 P_N` has both degrees 8 and `P_T^2 F_q P_N` has both degrees 10. The verifier computes both degrees from assembled matrices (weight `q` by two). Establish that the highest frequency coefficient remains nonzero at every finite boost. On degree-changing faces, redo both counts from the reduced original equations; do not carry the numbers 8 or 10 across the boundary. For constrained or mixed-order systems, justify the reduction and constraint propagation before applying this comparison. Degree equality is a necessary structural check here, not a stand-alone hyperbolicity or nonlinear causality theorem.

**Expected outputs.** Original matrix, sector/constraint transformations, simplest-sector bounds, longitudinal polynomial, conservation/gap inventory and principal matrices for every sector.

**Proceed when.** The reduced determinant reproduces the original one up to explicitly nonzero factors and all removed modes have a constraint or gauge justification. Every field or row transformation is invertible on its claimed domain.

**Failure modes and alternatives.** Dividing by \(s\), \(k\), a susceptibility or a characteristic polynomial can remove modes. Keep a separate branch at each zero, or use polynomial row operations and retain constraints. An identically zero determinant requires diagnosing gauge or constraint redundancy, not deleting an arbitrary equation.

**Save.** Original and reduced matrices, their transformation identity and determinant normalizations, constraint propagation equations, all zero-momentum factors, and directional principal symbols.

## Stage 4 Investigate longitudinal factorization possibilities

**Required inputs.** The original longitudinal polynomial, its small-momentum hydrodynamic roots, gap structure, derivative order, symmetry constraints, entropy equalities and bounds from the shear sector.

**Calculation.** Explore possible factorizations before committing to a preferred one. This is a search over admissible coefficient ansätze, not just a call to a symbolic factor routine after one assignment.

1. Record the polynomial's allowed monomials, parity or conjugation relations, temporal degree, spatial degree and lowest homogeneous ideal part. For this paper weight \(s,k\) by one and \(q\) by two. In anisotropic systems use all independent momentum components or direction invariants.
2. Enumerate candidate degree partitions compatible with that structure. A sextic might split into \(2+4\), \(3+3\), \(1+5\), \(2+2+2\), or smaller blocks; a quartic might admit \(1+3\) or \(2+2\). These are candidates, not assumptions of realizability. Respect the allowed derivative order of each proposed factor.
3. Allocate conservation roots and relaxation gaps to each factor at \(k=0\). Match the ideal sound and diffusive behavior at small momentum. Acoustic roots \(s\sim\pm i\sqrt{x}k\) cannot be reproduced by a product that has only ordinary diffusive roots \(s\sim-Dq\).
4. Introduce a polynomial factor ansatz with state/transport-dependent coefficients, fixed normalizations and the required conjugation properties. Coefficients may not depend on frequency, momentum or observer velocity in a local constitutive construction. Test even-momentum ansätze first when justified; if these fail, identify whether complex conjugate factors or odd signed-momentum terms remain allowed by the full polynomial's symmetry.
5. Form \(P_{\rm orig}-\mathcal N\prod_aF_a\), clear only denominators proved nonzero, and set every independent monomial coefficient to zero. Solve the matching equations jointly with entropy equalities. Keep case splits when a pivot, discriminant or leading coefficient vanishes. Track the quotient and the exact remainder on the original determinant.
6. Rank successful branches by regularity, freedom in physical transport, simplicity of stability conditions, shear compatibility, characteristic speeds and requested symmetry limits. A factorization that fixes prescribed transport to an unphysical value is a failed branch.

Maintain a factorization table with columns `candidate`, `root allocation`, `coefficient equations`, `denominators`, `entropy compatibility`, `remainder`, `remaining inequalities`, `domain`, and `status`.

### What the two fluid calculations teach

For a neutral fluid,

\[
P_N(0,q)=xw^2q+F_Lq^2,\qquad xw^2>0.
\]

A product of two standard diffusive telegrapher factors
\((\tau_a s^2+s+D_aq)(\tau_b s^2+s+D_bq)\)
has only a \(q^2\) term at \(s=0\). It cannot equal this neutral quartic up to a nonzero state-only normalization. This coefficient mismatch rejects that specific ansatz, not all quadratic factors.

A useful successful neutral branch instead sets \(\pi_2=4\eta/3\) and \(\varepsilon_2=0\):

\[
P_N=(\theta_1s+w)
\left[(w+x\varepsilon_1s)(s^2+xq)+\Gamma s q\right].
\]

The factor \(\theta_1s+w\) is a momentum-independent relaxation factor, and the remaining factor is an acoustic cubic. The shear polynomial is separately telegrapher-like. For \(\Gamma>0\), division of the original neutral quartic by \(s^2+xq\) leaves an \(s q\) term \(w\Gamma s q\); an exact undamped ideal-sound factor would contradict the prescribed attenuation.

The charged system has an additional diffusive hydrodynamic mode. Its successful split is instead

\[
P_{\rm ch}=-\frac{\Delta_J}{w}
(\tau_qs^2+s+D_qq)P_N.
\]

The quadratic carries one charge conservation root and one charge gap. The quartic carries two acoustic conservation roots and two gaps. It may remain coupled. It becomes a quadratic times a linear times a cubic only for the special neutral seeds above. A principal-part factorization, such as \(A_Ls^2(s^2+q)\), is not a factorization of the full damped sound polynomial.

The transferable method is to use physical root structure, entropy and matrix structure to select and test factor ansätze. The single-charge telegrapher form is the successful result in this model, not a universal template for new longitudinal systems.

**Expected outputs.** A classified list of candidate splits, solved branches or exact obstructions, and a chosen tractable polynomial/block structure with unresolved inequalities stated.

**Proceed when.** At least one branch satisfies exact matching and physical-input constraints, or a decision to analyze the unsplit polynomial has been documented.

**Failure modes and alternatives.** Distinguish `ansatz inconsistent`, `outside requested domain`, `computationally unresolved` and `counterexample to claimed family`. A nonzero remainder or negative bulk rejects that candidate only. Alternatives include another degree partition, retaining an irreducible quartic/sextic, a triangular matrix reduction, larger coefficient freedom, or a direct stability certificate. A general impossibility theorem requires exhausting the declared ansatz class and proving that it covers the proposed generality.

**Save.** Every factor ansatz and normalization, complete matching system, elimination branches, exact remainders, root allocations and any elimination certificate or counterexample. Preserve abandoned branches under distinct version IDs.

## Stage 5 Reduce inequalities and construct coefficients

**Required inputs.** Surviving factor/block structures or the unsplit original polynomial, entropy parametrization, simplest-sector bounds and required symmetry limits.

### Neutral reduction as a worked construction method

From the original neutral matrix, compute \(P_N=x\det M_N\), not a target polynomial:

\[
P_N=A_Ls^4+B_Ls^3+(w^2+C_Lq)s^2+D_Lqs+xw^2q+F_Lq^2,
\]

\[
\begin{aligned}
A_L&=x\varepsilon_1\theta_1,& B_L&=w(x\varepsilon_1+\theta_1),\\
C_L&=x[\varepsilon_1(4\eta/3-\pi_2)+\varepsilon_2(\theta_2+\pi_1)+\theta_1\pi_1],\\
D_L&=xB_L+w\Gamma,&F_L&=x\theta_2(\pi_2-4\eta/3),\qquad
\Gamma=4\eta/3+\zeta_*.
\end{aligned}
\]

Under \(w>0\), \(0<x<1\), \(\Gamma>0\), \(\varepsilon_1,\theta_1>0\), define

\[
R=D_L/B_L>x,\quad\Sigma=C_L/A_L,\quad\Phi=F_L/A_L,\quad
\mathcal L=R(\Sigma-R)-\Phi.
\]

Derive the Hurwitz minors directly:

\[
\begin{aligned}
\Delta_1&=B_L,\\
\Delta_2&=B_Lw^2+A_LB_L(\Sigma-R)q,\\
\Delta_3&=B_Lw^3\Gamma q+A_LB_L^2\mathcal L q^2,\\
\Delta_4&=(xw^2q+F_Lq^2)\Delta_3.
\end{aligned}
\]

All real \(q>0\) reduce to \(\Phi\geq0\), \(\mathcal L\geq0\); these imply \(\Sigma\geq R\). Necessity here follows from the highest powers of \(q\) and sufficiency from the positive lower powers. This is special low-degree algebra: positivity of every polynomial coefficient is generally sufficient but not necessary for positivity on an interval.

The principal polynomial in \(y=c^2\) is \(f(y)=y^2-\Sigma y+\Phi\). Since \(f(R)=-\mathcal L\leq0\), the roots interlace \(R\): \(0\leq y_-\leq R\leq y_+\). To put both in \([0,1]\), additionally require \(\Sigma\leq2\) and \(1-\Sigma+\Phi\geq0\). Alternatively choose desired \(0\leq y_-\leq y_+\leq1\) first, set \(\Sigma=y_-+y_+\), \(\Phi=y_-y_+\), and impose

\[
\mathcal L=(R-y_-)(y_+-R)\geq0.
\]

Then solve the resulting coefficient equations together with entropy and shear. Not every desired pair can be realized by regular coefficients; matching decides this.

### Solvable choices illustrated by the paper

- **Zero lower sound speed.** Set \(\pi_2=4\eta/3\), hence \(\Phi=0\), and solve \(x<R\leq\Sigma\leq1\). This removes a principal coefficient while retaining physical attenuation.
- **Relaxation times cubic.** Also set \(\varepsilon_2=0\). Entropy gives \(\pi_1=x\varepsilon_1+\Gamma/x\). The cubic's nontrivial RH margin is \(w\Gamma q\), and its nonzero squared characteristic speed is \(x+\Gamma/(x\varepsilon_1)\). Thus \(\varepsilon_1=\lambda\Gamma/[x(1-x)]\), \(\lambda\geq1\), solves the speed bound. The arbitrary \(\theta_2\) drops out of this determinant but not the matrix. Current F1 and F2 select \(\theta_2=0\) and \(\theta_2=\theta_1\).
- **Luminal design with nonzero scalar mixing.** Keep \(\varepsilon_2\ne0\), set \(\Sigma=1\), and solve
  \[
  \theta_2=\frac{(\varepsilon_1-\pi_1)\theta_1-\varepsilon_2\pi_1}{\varepsilon_2},\qquad
  x\varepsilon_1+\theta_1\geq\frac{\Gamma}{1-x}.
  \]
  This division demands a nonvanishing \(\varepsilon_2\) branch or a separately cancelled endpoint formula. Choosing positive scalar shares, rather than fixing \(\varepsilon_2\leq0\), permits the finite conformal F4 construction.
- **Use a known positive margin.** The balanced seed in `eq:balanced` has \(\varepsilon_2=\pi_1=m\). Increasing its vector coefficients yields F5 with \(x<R<\rho_0\leq\rho<1\). A bounded deformation \(\chi=\beta(3x-1)^2/[1+(3x-1)^2]\), \(0\leq\beta\leq1\), spends only part of the speed margin and vanishes at conformality. The explicit positive expression for \(\rho_0-R\) in `app:eq:charged-AS-R-margin` is the certificate; continuity alone is not.
- **Raise the lower sound speed.** F6 scales the balanced scalars by \(1<\Lambda\leq2\), fixes \(\pi_2=4\eta/3+(\Lambda-1)\Gamma\) through entropy, and obtains \(\Phi>0\). It proves \(\mathcal L=\mathcal L_0+\chi(1-\Sigma_0)(R-j)>0\) by the positive polynomial \(Q\) in `app:eq:charged-AN-positive-Q`. Together with \(\Sigma<1\), this gives \(0<y_-<R<y_+<1\). The bound \(\Lambda\leq2\) is a sufficient design choice, not a demonstrated maximal domain.

### Search algorithm for a new polynomial

Eliminate entropy equalities first, choosing pivots whose denominators stay nonzero on the required limits. Normalize by positive thermodynamic scales to reduce dimensions and parameter count. Compute exact RH determinants for real-coefficient factors and express them as polynomials in momentum magnitude and direction invariants. Look for cancellations, affine dependence, squares, factored positive expressions and interlacing relations. If a polynomial is positive on a compact direction interval, an exact Bernstein-basis certificate, Sturm decomposition or quantifier elimination may be useful. A rational sum-of-squares certificate is sufficient where found; failure to find one is not proof of instability. A floating optimization result must be rationally reconstructed and verified as an exact identity with domain multipliers.

Design principal speeds and damping together. A principal factorization does not constrain all lower-order terms. If using perturbation of a known frame, prove bounds uniformly over the momentum and direction domain after treating small momentum, large momentum and degeneracies. Pointwise continuity does not supply a single admissible deformation size.

For an explicit example of a positivity decomposition, F5 uses
\[
d_5=8x(1-x)+\lambda(1+x)^2,\qquad
\rho_0-R=\frac{(1-x)[8x(1-x)+\lambda(\lambda+1)(1+x)^2]}{2\lambda d_5}>0.
\]
Every factor has a proved sign on \(0<x<1,\lambda>1\). The accompanying script checks this identity and F6's positive \(Q\) decomposition exactly. It is this combination of an exact identity and a domain sign argument that turns a search result into a certificate.

Impose requested symmetry limits during the search. For this project set
\(p=T^4 f(\mu/T)+\ell g(T,\mu)\) and require finite coefficients as \(\ell\to0\), \(\zeta\to0\), with regular limiting state data. Check absolute residuals

\[
\varepsilon_i-3\pi_i,\quad\pi_1-3\pi_2,\quad\nu_1-3\nu_2,\quad
\theta_1-\theta_2,\quad\gamma_1-\gamma_2\longrightarrow0.
\]

The neutral endpoint is \((3\Pi,\Pi,\Pi,\Pi/3,\theta,\theta)\). A single exactly conformal solution is not an approach theorem. Record allowed relative rates of \(\ell\), transports and parameters; prove regularity for every permitted approach, not only one path. Prohibit division by \(B,q_T\) or vanishing transport without a removable-singularity proof. In new systems derive the relevant symmetry identities rather than importing these coefficients or the spatial factor \(4/3\).

**Expected outputs.** Explicit coefficient functions, parameter domain, denominator ledger, entropy residuals, exact positivity decompositions, characteristic bounds and symmetry-limit formulas.

**Proceed when.** The candidate is defined throughout its claimed domain and its remaining analytic obligations are explicit. A numerical promising point may proceed as a conjectural candidate, but not as a verified family.

**Failure modes and alternatives.** Overconstrained speed matching, incompatible conformal residuals, or a hidden transport restriction require another branch. Relax the ansatz, not the user's physical requirements. A bound proved only for one direction or state must be recorded at that scope.

**Save.** Elimination equations, assumptions used in each sign, exact positive decompositions, candidate formulas, all singularity branches, limit expansions and rejected alternatives.

## Stage 6 Derive autonomous fluctuations and coefficient maps

**Required inputs.** The full original matrix, ideal thermodynamic couplings, entropy constraints and the factorization candidates from Stage 4. This stage can feed a successful matrix ansatz back into Stages 4–5.

### Reconstruct the charged map

The paper's thermodynamic variables satisfy

\[
E=\partial_T\epsilon|_\alpha,\ F=\partial_\alpha\epsilon|_T,
\ N=\partial_Tn|_\alpha,\ H=\partial_\alpha n|_T,\quad
q_T=N-rE,\quad q_\alpha=H-rF.
\]

Form the charge fluctuation \(h=\delta n-r\delta\epsilon=q_T\delta T+q_\alpha\delta\alpha\) and subtract \(r\) times the original energy row from the original charge row. Its ideal velocity contribution cancels because \(n-rw=0\). Seek, rather than presume, the identity

\[
\mathcal R_n-r\mathcal R_\epsilon
=(\tau_qs^2+s+D_qq)(q_T,q_\alpha,0).
\]

Matching the coefficients of \(s^2,q,ik s\) gives

\[
\begin{aligned}
\nu_1-r\varepsilon_1&=T\tau_qq_T,&\nu_3-r\varepsilon_3&=\tau_qq_\alpha,\\
\gamma_2-r\theta_2&=-TD_qq_T,&\gamma_3-r\theta_3&=-D_qq_\alpha,\\
\nu_2+\gamma_1&=r(\varepsilon_2+\theta_1).
\end{aligned}
\]

Add the vector entropy relation, not an unnecessary equality \(\theta_1=\theta_2\). The pressure one-form
\(dp/w=dT/T+rT\,d\alpha\) suggests a representative
\(\varepsilon_3=rT\varepsilon_1\), \(\pi_3=rT\pi_1\), \(\theta_3=rT\theta_2\). This makes the energy–momentum block on \(h=0\) identical to a neutral block with charged \(w,x\). The remaining coefficients are

\[
\begin{aligned}
\nu_1&=r\varepsilon_1+T\tau_qq_T,&\nu_2&=r\varepsilon_2+TD_qq_T,&
\nu_3&=r^2T\varepsilon_1+\tau_qq_\alpha,\\
\gamma_1&=r\theta_1-TD_qq_T,&\gamma_2&=r\theta_2-TD_qq_T,&
\gamma_3&=r^2T\theta_2-D_qq_\alpha.
\end{aligned}
\]

Derive \(F=T^2N\), \(A=wq_\alpha/(T\Delta_J)\), \(B=-wq_T/\Delta_J\), and
\(\Xi=q_\alpha-rT^2q_T=T\Delta_Jx/w>0\) from thermodynamics. Entropy then fixes

\[
D_q=\frac{\mathcal D T}{\Xi},\qquad
\zeta_*=\zeta+\frac{\mathcal D T^2B^2}{x},\qquad
\Gamma=4\eta/3+\zeta_*.
\]

Evaluate the neutral seed at this \(\zeta_*\), keeping the physical charged \(\zeta\) prescribed. For \(D_q>0\), select \(\tau_q=\alpha_qD_q\), \(\alpha_q\geq1\). The auxiliary positive bulk shift compensates the charge contribution to the charged bulk invariant; using the unshifted seed generally fails matching. Conductivity \(\mathcal D\) and mode diffusivity \(D_q\) are different quantities.

The change of amplitudes \((\delta T,\delta\alpha)\mapsto(\delta\epsilon,h)\) has determinant \(\Delta_J\). With equation/column order recorded, the remaining block has determinant \(P_N/w\), and expansion of the original matrix gives

\[
\det M_{\rm charged}=-\frac{\Delta_J}{w}(\tau_qs^2+s+D_qq)P_N.
\]

This must be checked by an exact difference and polynomial remainder, including its normalization. Do not infer it merely from the proposed roots. It is a linear equilibrium row identity; it does not assert autonomous nonlinear evolution of \(h\), and the pressure one-form need not be a globally integrable field coordinate.

### What can generalize

Search for left row combinations \(\ell_a\mathcal R_a\) that cancel ideal coupling to the other amplitudes. Then solve coefficient identities making the selected fluctuation or vector of fluctuations autonomous. More generally seek invertible transformations \(L M_{\rm orig}R\) with block-triangular form. Save both transformations and all nonzero determinants. Avoid rational Schur complements that divide by a polynomial whose roots are physical unless those roots are restored and checked.

For several charges, plausible trial fluctuations are \(h_a=\delta n_a-(n_a/w)\delta\epsilon\), but susceptibility and dissipative matrices must be derived afresh. One may obtain a matrix relaxation–diffusion block instead of independent scalar telegraphers. Simultaneous diagonalization, positivity of individual eigenvalues, or a scalar bulk correction must not be assumed: noncommuting matrices and cross-couplings remain part of the problem. The pressure-gradient representative and the scalar \(\Xi\) are specific to the present single-charge structure.

Within the paper's fixed row ansatz, additional changes
\((\delta\varepsilon_1/T,\delta\varepsilon_3)=f_E(q_T,q_\alpha)\), with analogous \(f_P,f_Q\) changes and compensating current changes, affect only coupling into the autonomous charge column. They preserve determinant and entropy. The inverse decomposition uses \(\Xi\), and finite conformal matching requires \(f_E-3f_P\to0\) for finite functions. This is an example of finding unused frame freedom after a reduction. In a new system recompute this null space and its effect on eigenvectors; no three-function count is universal.

**Expected outputs.** A proved row/block identity, admissible coefficient map, transport compensation, Jacobian/normalization factors and residual freedom, or a documented failure to isolate such a block.

**Proceed when.** The original matrix identity and all entropy residuals vanish exactly, no physical input has been traded away, and the map is regular on the claimed domain.

**Failure modes and alternatives.** Failure of an autonomous scalar row does not exclude determinant factorization by another mechanism. Return to general matching, try a larger coupled block, or analyze the unsplit polynomial. A singular scalar susceptibility calls for a separate domain or chart, not a numerical fallback formula.

**Save.** Original row combinations, monomial equations, transformations, exact determinant difference and factor remainders, entropy calculation, inverse parametrization and precise completeness scope.

## Stage 7 Verify original identities and rest stability

**Required inputs.** A versioned candidate with explicit domain, the independently retained original equations, and the expected factors and inequalities.

**Calculation.** Recompute the candidate's original matrix and entropy from its coefficients. Do not reuse the proposed factor product as the determinant implementation. If two implementations are used, state whether they were independently derived or share an algebraic backend.

Perform these exact checks:

1. All original constraints and thermodynamic identities hold, and the transport residuals vanish.
2. The original determinant minus the claimed normalized product is zero coefficient by coefficient. Divide the original polynomial by each claimed factor and save the zero remainder and correct quotient. A zero remainder alone does not establish the claimed normalization, quotient or multiplicities.
3. Recover physical small-momentum coefficients from the original equations. In this construction sound has \(s_\pm=\pm i\sqrt{x}k-\Gamma k^2/(2w)+O(k^3)\) and charge \(s=-D_qq+O(q^2)\); the charged sound attenuation uses the derived auxiliary \(\Gamma\). An undamped target at positive required attenuation fails this check.
4. At \(k=0\), extract only the proved conservation factors, check the remaining gaps with a positive leading normalization, and compare null spaces with conservation counting.
5. For every real nonzero momentum and direction, prove strict root location when damping is expected. For real polynomials use the correct RH minors; for marginal branches use Stage 9. Establish signs over the entire state, transport, momentum and direction domain, not a set of sample points.
6. Recompute all principal characteristic factors from the original symbol and verify real roots and \(|c|\leq1\). Include transverse, constraint and degenerate sectors, not only the longitudinal determinant.

For a real degree-\(m\) polynomial with positive leading coefficient, the paper's transposed Hurwitz construction is
\(H_{i\ell}=a_{m+i-2\ell}\), \(1\leq i,\ell\leq m\), with out-of-range coefficients zero. Strict stability requires every leading determinant positive. Confirm a new implementation on simple stable and unstable polynomials before using it in a search.

**Expected outputs.** Exact identity certificates, analytic rest-stability and speed proofs, zero-momentum gap checks, and a list of remaining boost or boundary obligations.

**Proceed when.** Every claimed identity is exact, universal signs have analytic certificates, and the candidate is labeled only with the scope actually proved. An unresolved sign remains unresolved.

**Failure modes and alternatives.** Negative minors, entropy residuals or a nonzero original remainder reject the proposed claim. A sufficient positivity test failing may only mean that test is inconclusive; distinguish this from an actual necessary-condition violation. Use an exact root-count method or refine the parameter domain without concealing the restriction.

**Save.** All residuals, coefficient arrays, quotient/remainder pairs, RH matrices/minors, leading-coefficient signs, root-count proofs, domain substitutions and any exact counterexample.

## Stage 8 Prove boosts and every propagation direction

**Required inputs.** Rest matrix and full covariant equations, a rest-stability proof, sector factor identities valid as polynomial identities, and all characteristic restrictions.

### Construct the laboratory polynomial and its gaps

For an isotropic rest state orient the boost along \(z\), keeping general real \(k_z,k_\perp\). Use both transformed arguments:

\[
s'=\gamma(s+ivk_z),\qquad q'=k_\perp^2+\gamma^2(k_z-ivs)^2,\qquad
\gamma=(1-v^2)^{-1/2}.
\]

Verify this substitution against direct linearization at a moving background, including transformations of amplitudes and equations. In a new anisotropic system transform the background vectors/tensors as well, and retain all independent relative angles. A rest-frame real-momentum proof cannot be applied to these generally complex transformed momenta.

At actual laboratory \(\mathbf k=0\), extract \(P_{\rm boost}(s,0)/s^m\), where \(m\) is the established conservation multiplicity on that branch. For the charged longitudinal sextic \(m=3\); the conventional normalization includes \(\gamma^3\). Direct extraction in the paper yields

\[
\frac{P_{{\rm ch},\rm boost}(s,0)}{\gamma^3s^3}
=-\frac{\Delta_J}{w}(1+\ell_qs)(a_gs^2+b_gs+c_g),
\]

\[
\ell_q=\gamma(\tau_q-D_qv^2),\quad
a_g=\gamma^2(A_L-C_Lv^2+F_Lv^4),\quad
b_g=\gamma(B_L-D_Lv^2),\quad c_g=w^2(1-xv^2).
\]

For the regular dissipative branch these are positive because
\(A_L-C_Lv^2+F_Lv^4=A_L(1-y_-v^2)(1-y_+v^2)>0\), \(R\leq1\), and \(\tau_q\geq D_q>0\). After removing the nonzero overall normalization, the cubic has

\[
b_3=\ell_qa_g,\ b_2=a_g+\ell_qb_g,\ b_1=b_g+\ell_qc_g,\ b_0=c_g,
\quad b_2b_1-b_3b_0=b_g(a_g+\ell_qb_g+\ell_q^2c_g)>0.
\]

Check the leading sign too. Boosting an individual rest \(k=0\) mode does not calculate these laboratory gaps.

### A direct complex-polynomial proof template

The neutral proof is reusable only after rederiving its ingredients for the new polynomial:

1. **Stable starting point.** Fix an arbitrary real laboratory momentum and final finite boost. At zero boost use the proved rest root count.
2. **No imaginary-axis crossing.** Set \(s=i\sigma\), \(\sigma\in\mathbb R\). Now \(s'=i\Omega\) and \(q'=K^2\geq0\) are real-frequency/rest-momentum variables. For the quartic,
   \[
   \Im P_N=\Omega(-B_L\Omega^2+D_LK^2).
   \]
   If \(\Omega=0\), then \(\Re P_N=xw^2K^2+F_LK^4>0\) at nonzero momentum. If \(\Omega^2=RK^2\), then
   \[
   \Re P_N=w^2(x-R)K^2-A_L\mathcal L K^4<0.
   \]
   The only simultaneous \(K=\Omega=0\) corresponds to the zero laboratory covector. This excludes crossings for every nonzero real laboratory momentum. For shear and charge, the imaginary parts are respectively \(w\Omega\) and \(\Omega\), and the remaining real terms at \(\Omega=0\) are positive for positive shear and diffusion.
3. **No root through infinity.** Along the closed segment joining zero to any fixed \(|v_*|<1\), prove a nonzero leading coefficient, continuity and boundedness of all normalized coefficients. The quartic's leading coefficient is \(\gamma^4A_L(1-y_-v^2)(1-y_+v^2)>0\). A Cauchy root bound then prevents loss or gain of roots at infinity.
4. **Conclude the root count.** Stable roots cannot leave the left half-plane. The momentum, direction and final finite boost were arbitrary, so the result is universal on the stated domain. This argument does not require a uniform bound as \(v_*\to1\), but a proposed uniform deformation theorem would require additional estimates.
5. **Handle marginal factors and zero momentum separately.** Exact advective or wave factors can remain on the imaginary axis. They invalidate a strict no-crossing premise unless removed with justified multiplicities and checked separately.

If this route does not close, derive a valid complex-coefficient criterion. One exact alternative is ordinary RH on
\(p(s)\overline p_{\rm coeff}(s)\), whose roots are those of \(p\) and their conjugates. Normalize \(p\) to monic using its proved nonzero leading coefficient. This doubles degree and is called **RH of the coefficient-conjugate product**, not direct Bilharz. If explicit Bilharz minors are required, implement and independently validate the authentic construction. Realifying an ordinary complex Hurwitz matrix produces squared moduli of its minors and is invalid as a sign test.

### Directional causality

For each isotropic squared rest speed \(y\in[0,1]\), derive the laboratory equation

\[
(1-yv^2)c^2-2v(1-y)\cos\phi\,c
+v^2\cos^2\phi-y(1-v^2+v^2\cos^2\phi)=0.
\]

Check its discriminant and leading sign for every \(\phi\) and finite boost. The invariant relation \(|\mathbf k|^2-\omega^2=(1-y)|\mathbf k'|^2\geq0\) establishes \(|c|\leq1\) for this factor. At \(y=0\), \(c=v\cos\phi\); at \(y=1\), \(c=\pm1\). Apply it to all sound, shear and charge factors actually present.

For anisotropic systems derive the full directional principal symbol and its hyperbolicity cone instead of reusing this quadratic. Prove real characteristic roots and the requested speed bound for every unit wavevector and background orientation. For a claim about signal/domain-of-dependence causality, also establish the relevant cone or ray inclusion; a few phase speeds or group velocities on symmetry axes are insufficient. Constraint characteristics and coincident cones must be included.

**Expected outputs.** Original laboratory polynomial, direct gap polynomial, an analytic all-real-momentum/all-finite-boost root-count proof, and all-direction characteristic bounds.

**Proceed when.** Both finite roots and possible roots at infinity are controlled, gaps have the correct degree and signs, and every relevant direction and constraint sector is included.

**Failure modes and alternatives.** A crossing equation without a sign proof is an unresolved gap. A zero leading coefficient requires a separate lower-degree branch. A boost computation at one velocity or angle is diagnostic only. Covariance is useful to construct the polynomial and transform proved cones; it does not substitute for this stability calculation.

**Save.** Boost convention, direct moving-background comparison, complex coefficients, real/imaginary crossing equations, resultants if used, leading-coefficient bounds, root-count continuation argument, laboratory gaps and directional speed certificates.

## Stage 9 Resolve boundaries and separate levels of claim

**Required inputs.** Candidate formulas before division, all domain faces, symmetry limits, and lists of repeated, zero and luminal principal roots.

**Calculation.** Stratify the domain by vanishing transports, pivots, leading coefficients and discriminants. Substitute each boundary into the original matrix first. Recompute temporal degree, conservation multiplicity, constraints, actual principal system and gaps. Analyze intersections of boundary faces, not just each face separately.

For this paper the essential cases are listed below. [BOUNDARY_ANALYSIS.md](BOUNDARY_ANALYSIS.md) supplies explicit reduced polynomials and their direct boost arguments, including the cubic branch summarized in the final paper's footnotes:

| Boundary | Required calculation and interpretation |
|---|---|
| \(\eta=0\), \(\theta_1>0\) | Shear becomes \(s'(\theta_1s'+w)\): an advective marginal mode and a damped gap. It has zero comoving characteristic speed. |
| \(\eta=\theta_1=0\) | Shear is first order, \(ws'=0\). Do not use \(\eta/\theta_1\). Numbered neutral seeds can also lose one sound degree. |
| \(\mathcal D=0\), finite \(\alpha_q\) | The named prescription gives \(D_q=\tau_q=0\), hence \(F_q=s'\). The longitudinal gap cubic loses a degree. |
| \(D_q=0\), independent \(\tau_q>0\) | The broader row ansatz permits \(F_q=s'(1+\tau_qs')\). This is a different boundary prescription with a retained damped gap. |
| \(\Gamma=0\) | Nonnegative summands imply \(\eta=\zeta=0\), \(\mathcal D B^2=0\). Regular F4–F6 seeds reduce to ideal sound, possibly with a charge telegrapher when \(\mathcal D>0,B=0\). Disappeared quartic modes have no assigned speed ratios. |
| \(\mathcal L=0\) or \(y_+=1\) | Positive lower powers may keep all finite-momentum RH minors strictly positive. Verify the first nonzero damping correction and the boosted leading coefficient. Do not exclude causal saturation. |
| Repeated principal roots or \(y_-=0\) | Derive a dominant-balance expansion from the original polynomial; a simple-root large-momentum formula may divide by zero. Analyze the original pencil's eigenspaces for any bounded-evolution claim. |
| \(\Delta_J=0\), \(x=0\) or \(x=1\) | Outside the map's present coordinate/domain certificate. Treat as a new chart or separate problem if coverage is requested; do not declare them covered by continuity. |

For a fixed nonzero polynomial, closed-left-half-plane spectral location can be tested exactly by applying strict RH to \(p(s+\varepsilon)\) for sufficiently small \(\varepsilon>0\), or to its coefficient-conjugate product when coefficients are complex. The original roots shift left by \(\varepsilon\). Determine each minor's sign from its first nonzero \(\varepsilon\) coefficient with exact arithmetic. A symbolic sign that cannot be proved stays unknown; a pointwise shift result is not a uniform parameter proof.

Merely replacing strict RH inequalities by non-strict ones fails: \(s^2-1\) has vanishing Hurwitz minors but a positive root. Nonnegative coefficients do not fix the general problem. At marginal roots, compare algebraic and geometric multiplicities in a justified evolution reduction; polynomial root location alone cannot exclude Jordan growth.

For large momentum, expand every simple propagating branch as \(s=\pm i\sqrt y\,k+d+\cdots\). For the paper's quartic,
\(d=(B_Ly-D_L)/[2(C_L-2A_Ly)]\). If this vanishes, continue to the first nonzero real term. If roots coalesce, use a separate scaling or exact factorization. Also inspect bounded zero-speed branches and any fractional-power behavior. Principal real roots do not by themselves rule out divergent subleading growth.

Keep four distinct claims in the ledger: (i) linear spectral location; (ii) bounded linear evolution and appropriate uniform estimates; (iii) characteristic/cone causality; (iv) nonlinear local existence, uniqueness and continuous dependence in a specified function class. For a nonlinear extension derive the variable-state principal system, compatible initial/constraint data, an appropriate hyperbolic reduction or energy/regularity proof, and recovery of the original equations. Check theorem hypotheses coefficient by coefficient if using a PDE theorem. Gevrey existence is not Sobolev well-posedness, and local well-posedness is not nonlinear stability. The all-boost spectral proof must still be direct as above.

**Expected outputs.** A complete boundary table with reduced equations, residual modes and gaps, marginal-mode classification, finite symmetry limits and separate nonlinear obligations.

**Proceed when.** Every boundary included in the advertised domain has a direct analysis, and stronger claims are either proved or explicitly left open.

**Failure modes and alternatives.** A boundary may violate an extra request for nonzero speeds without violating the original nonnegative-transport problem. Report the incompatibility rather than replacing zero transport by a positive regulator. If order changes obstruct a nonlinear theorem, retain the linear boundary result at its actual scope.

**Save.** Boundary substitutions into original matrices, degrees before/after, exact factors, asymptotic balances, eigenspace checks, pathwise or domain-wide limit proofs, and a list of excluded versus unresolved cases.

## Stage 10 Package evidence and maintain the proof ledger

**Required inputs.** All preceding outputs, including failures, exact scripts, analytic proofs and diagnostic examples.

**Calculation.** Assign a stable system/family/version ID. Freeze the source hash, assumption set and coefficient map for each claim. Make the ledger a dependency graph: changing a coefficient invalidates downstream entropy, matrix, stability, boost and boundary claims until they are rerun or proved invariant. A determinant-preserving change may inherit spectral results only after an exact original-matrix identity valid for complex arguments; eigenspace and nonlinear claims remain separate.

Use four primary claim statuses, with evidence type recorded independently:

| Status | Meaning and required evidence |
|---|---|
| Established identity | Exact algebraic statement under listed identities and denominator assumptions; save original expressions and zero residuals. It is not automatically a physical-domain theorem. |
| Conditional result | An explicit analytic implication from enumerated hypotheses, with all sign, degree and boundary steps supplied. State which candidate satisfies the hypotheses. |
| Conjecture | A proposed pattern, generalization or candidate supported by incomplete analysis or finite diagnostics. State the next calculation that could prove or refute it. |
| Unresolved gap | A specific missing argument needed for an advertised claim; record the dependency it blocks and the alternative route. |

Record failed ansätze and exact counterexamples alongside these statuses, preserving the rejected claim and its scope. A `PASS` from a numerical sample is never a universal proof status.

A machine-readable claim entry should contain:

```json
{
  "claim_id": "system_family_v1.boost_stability",
  "statement": "All physical roots have Re(s)<=0 for the stated domain",
  "status": "unresolved_gap",
  "quantifiers": ["all admissible states", "all real lab momenta", "all finite boosts", "all directions"],
  "assumptions": [],
  "depends_on": ["original_matrix", "entropy_matching", "rest_root_count"],
  "source_hashes": {},
  "analytic_proof": null,
  "exact_checks": [],
  "diagnostics": [],
  "boundary_coverage": [],
  "next_required_calculation": "Exclude imaginary-axis crossings and roots through infinity",
  "excluded_claims": ["nonlinear stability", "Sobolev well-posedness"]
}
```

For each exact check save inputs, assumptions, polynomial coefficient arrays, transformations, quotient/remainder, normalization and output. For every numerical calculation save rational or explicitly exact algebraic inputs, actual precision, solver/version, roots, multiplicities, absolute residuals and scaled residuals. A useful scaled residual is

\[
\frac{|p(s_*)|}{\sum_j|a_j||s_*|^j},
\]

with exact zero handled separately. Preserve solver failures. Increasing precision after converting a machine float does not restore its lost digits.

Include tests deliberately capable of failing: an unstable polynomial that fools non-strict minors; an entropy-violating factor ansatz; a wrong factorization remainder; zero-momentum gaps; zero transports; luminal saturation; and at least one oblique boost. A finite diagnostic set helps find mistakes and validate implementation, but supplies no universal quantifier.

**Expected outputs.** A protocol-compliant candidate packet with an executable entry point, human-readable proofs, machine-readable ledger, exact verification, diagnostics and a manifest.

**Proceed when.** Another AI can reproduce each established identity, locate each analytic argument and identify every unproved extension without relying on conversation history.

**Failure modes and alternatives.** Missing logs mean a calculation is not evidenced; rerun it or mark it unverified. Contradictory versions require distinct IDs and an explicit supersession record. Preserve original failed searches and do not adjust tolerances to force success.

**Save.** At minimum `problem_spec`, `assumptions`, `coefficients`, `original_matrices`, `factorization_search`, `entropy`, `rest_proof`, `boost_proof`, `boundary_cases`, `proof_ledger`, `exact_checks`, `examples`, `environment`, `run.log`, and a SHA256 manifest. New work belongs in versioned files; manuscripts are modified only under a separate instruction.

The execution logic is:

```text
derive original equations, entropy invariants, constraints and domain
derive sector decomposition; analyze shear or other autonomous simple blocks
for each longitudinal factor/block ansatz compatible with the ideal modes:
    solve coefficient matching together with fixed-transport equalities
    split zero-pivot cases; record every discarded branch and its reason
    if matching is inconsistent: reject this ansatz branch and continue
    solve remaining all-momentum and directional inequalities analytically
    construct coefficient functions and prove requested limit regularity
    recompute entropy and determinant from original equations
    if any exact residual is nonzero: reject the candidate claim
    prove rest roots, actual boosted gaps, crossings and infinity control
    resolve every boundary included in the candidate domain
    save the scoped proof, exact examples and remaining gaps
if no factor ansatz succeeds:
    analyze the unsplit polynomial or a larger matrix block
    report unresolved construction, not general nonexistence
```

## Reproducible examples supplied with this protocol

The executable [verify_protocol.py](../scripts/verify_protocol.py) assembles the neutral and charged matrices explicitly rather than importing the candidate constructors. It checks selected generic algebra, including the neutral determinant and RH reduction, the linear-times-cubic branch, the obstruction to an undamped sound factor, the charged row identity and original-determinant remainders, entropy compensation, the boosted gap identities and the imaginary-axis reduction. It keeps charge relaxation independent in the generic calculation.

Its thermodynamic chart obeys the pressure identities and uses

\[
A=x-rT B,\quad E=\frac{w}{Tx}+\frac{T\Delta_JB^2}{wx},\quad
N=rE-\frac{\Delta_JB}{w},\quad F=T^2N,\quad
H=rF+\frac{T\Delta_JA}{w}.
\]

The script checks \(EH-FN=\Delta_J\). These are local algebraic data for identity checking, not a claim that arbitrary freely chosen values define one global EoS or meet every positivity assumption.

Three exact-input examples use
\(p(T,\mu)=T^4+T^2\mu^2+\ell T^2\), \(T_0=1\), \(\mu_0=1/2\), manuscript F6 (`paper-F6`), and \(\Lambda=\alpha_q=2,\beta=1\):

| Example | \(\ell\) | \(\eta,\zeta,\mathcal D\) | Purpose |
|---|---:|---|---|
| Conformal benchmark | 0 | \((1/5,0,1/10)\) | Recover the paper's finite coefficients and conformal relations; the expected squared speeds are \((1/12,2/3,1/16,1/2)\). |
| Nonconformal unequal vectors | \(1/7\) | \((1/5,1/10,1/10)\) | Exercise nonzero bulk compensation and unequal vector coefficients with a consistent EoS. |
| Conformal zero transport | 0 | \((0,0,0)\) | Recompute the lower-degree charged Euler polynomial and its conservation modes. |

Each example saves the exact matrix, coefficients, original rest polynomial, obliquely boosted polynomial and actual laboratory-zero-momentum gap polynomial. The boost is \(v=4/5\), so \(\gamma=5/3\), with \(k_z=2/3\), \(k_\perp=1/2\). Roots and residuals use 80 decimal digits, starting from exact inputs. These examples demonstrate the verification workflow, not the all-state or all-boost proof.

From the extracted package root, follow [README.md](../README.md) to create a clean environment and install the exact dependency pins. Then run:

```sh
python -m unittest discover -s tests -v
python scripts/check_package.py
python scripts/verify_protocol.py
```

The verifier creates a fresh directory under `generated/` and refuses an existing destination. It reads rational examples from [examples/inputs.json](../examples/inputs.json). Frozen [reference results](../reference_results) and manuscript files are never overwritten. The symbolic checks cover selected identities, not every argument in the manuscript. Tests use only the standard library plus the two pinned numerical/symbolic packages; no parent project, archived searches or Wolfram installation is needed. See [VALIDATION.md](../reference_results/VALIDATION.md) for the actual isolated archive test and its scope.

## Initial proof ledger for the extracted method

This ledger distinguishes calculations reproduced here from arguments read and reconstructed from the frozen manuscript. It is not a replacement for a future system's own ledger.

| ID | Status | Evidence and scope |
|---|---|---|
| I1 | Established identity | Neutral original determinant, RH polynomial identities and the specified linear-times-cubic remainder; reproduced by the new script. |
| I2 | Established identity | Charged original row identity, determinant normalization/remainders and transport compensation in the regular thermodynamic chart; reproduced by the new script. |
| I3 | Established identity | Laboratory sound-gap identity, charged gap-cubic RH identity and neutral imaginary-axis expression; reproduced by the new script. |
| I4 | Established identity | Finite rational conformal example and zero-transport degree reduction; exact example checks, with numerical roots only as diagnostics. |
| I5 | Established identity | Original charged determinant, charge row and entropy invariants preserved by three independent symbolic coefficient shifts; exact checks in the executable. |
| C1 | Conditional result | The neutral quartic inequalities imply strict finite-nonzero-momentum rest stability when \(w,x,\Gamma,A_L,B_L\) satisfy the stated positivity/domain assumptions. The analytic sign argument is in Stage 5 and the frozen manuscript. |
| C2 | Conditional result | C1 plus causal characteristic bounds and the direct gap/no-crossing/no-infinity arguments give all-finite-boost spectral stability for the paper's isotropic polynomial structure; reconstructed in Stage 8. This is not an independent formal verification of the whole manuscript. |
| C3 | Conditional result | A regular charged coefficient map transfers C1/C2 to a seed with the compensated auxiliary bulk, after original-matrix and entropy checks; zero transports require the separate branch arguments. |
| C4 | Conditional result | Fixed-row deformations preserve spectral polynomials if the exact triangular identity holds. The executable now checks the original shifted determinant, row identity and all three entropy residuals with independent symbolic shift functions. Eigenvector claims do not follow. |
| C5 | Conditional result | The explicit reduced cubic, ideal-wave, advective and relaxation factors in [BOUNDARY_ANALYSIS.md](BOUNDARY_ANALYSIS.md) have stable spectra and causal characteristics under their stated boundary assumptions. Bounded marginal evolution remains separate. |
| G1 | Unresolved gap for reuse | The stronger general quadratic-factor obstruction is not independently rederived by this protocol. Derive a complete elimination proof for the stated ansatz before using that classification as a search exclusion; no private notes are required or supplied. |
| G2 | Unresolved gap for each new system | New constraints, directional principal roots, complex boosted stability and degree-changing boundaries require new calculations. No existing neutral/charged theorem fills these rows automatically. |
| Q1 | Conjecture | Autonomous dissipative fluctuations or triangular blocks may simplify MHD, superfluid, multiple-charge or anisotropic frame construction. Their existence and transport-compatible realization are not assumed. |
| G3 | Unresolved gap for stronger claims | Nonlinear causality, bounded marginal evolution, strong hyperbolicity and local/global nonlinear evolution need separately specified proofs and hypotheses. |

## Application choices after extracting the method

No application is selected in this protocol. Before choosing one, prepare its Stage 1 specification and a preliminary Stage 3 sector inventory. The useful comparison is the tractability of the original equations and their constraints, not an expectation that every longitudinal determinant has a telegrapher factor.

| Candidate | Questions to resolve before starting its frame search |
|---|---|
| Magnetohydrodynamics | Which electromagnetic or flux variables are dynamical? What formulation and magnetic constraint are used? Which transverse sectors remain autonomous for oblique propagation? How are anisotropic viscosity/resistivity matrices prescribed? |
| Superfluid | What are the independent normal and superfluid variables, Josephson relation and phase/integrability constraints? What background relative flow is admitted? How do sound and transverse sectors mix? |
| Multiple charges | What is the susceptibility matrix and its regular domain? Which conductivity cross-terms are prescribed? Can charge-minus-energy combinations form a closed matrix block without changing those inputs? |
| Anisotropic fluid | Is the preferred direction fixed, externally sourced or dynamical? What residual symmetry remains? Which direction invariants enter the original matrix, and where do constraint or mode degeneracies occur? |

These are specification questions and candidate calculations, not results imported from the single-charge construction.

## Instructions to hand to the next AI

Read the package [AGENTS.md](../AGENTS.md), [CONVENTIONS.md](CONVENTIONS.md), [VERIFICATION_REQUIREMENTS.md](VERIFICATION_REQUIREMENTS.md), and source/evidence manifest. Start a separate study using the templates; never edit the frozen manuscript or reference evidence. Do not select an application without a physical specification. Execute Stages 1–3 first, proving any sector decomposition and analyzing shear or another autonomous simple sector before the longitudinal search. At Stage 4 compare multiple admissible factorization structures against the original polynomial and its hydrodynamic roots. Use Stages 5–6 to derive coefficients and maps; do not impose the charged map on a different system by analogy.

At each stage produce the required artifacts and update the ledger. Keep physical transport prescribed, retain constraints, and treat failed ansätze as local failures. Before claiming a family, complete original-matrix and entropy checks, an analytic all-real-momentum/all-finite-boost proof, every relevant directional characteristic check and every boundary included in the claim. Report a specific unresolved proof obligation when one remains. Supply exact executable examples, but never promote their sample results into a universal statement.
