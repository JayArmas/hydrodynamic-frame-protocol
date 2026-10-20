# Reduced polynomials and boundary proofs

These calculations expand the final manuscript's [neutral](PAPER_SOURCE.html#fn:neutral-zero-transport), [shear](PAPER_SOURCE.html#fn:shear-zero-transport), [charged](PAPER_SOURCE.html#fn:charged-zero-transport), and [independent relaxation](PAPER_SOURCE.html#fn:independent-charge-relaxation) footnotes. They concern linear spectra and characteristic speeds. They do not claim bounded evolution at repeated roots or nonlinear well-posedness. Each boundary must be imposed before using divided quartic invariants.

## Zero shear with positive attenuation

For paper-F1, F2 and F3 at eta=0 and Gamma>0, theta1=0, eps2=pi2=0 and pi1=x eps1+Gamma/x. Theta2 can remain nonzero in F3 but cancels from the determinant. Direct substitution into the original neutral matrix yields

\[
P_N=w C,\qquad C=a s^3+w s^2+b q s+xwq,
\quad a=x\varepsilon_1>0,\ b=x^2\varepsilon_1+\Gamma.
\]

The remaining squared sound speed is `y=b/a=x+Gamma/(x eps1)`. The family's bound makes `x<y<=1`. For every q>0 the cubic has positive coefficients and RH margin `w(b-a x)q=w Gamma q>0`. At q=0, `C=s^2(a s+w)`, giving two conservation roots and one damped gap. This reduction is checked from the original matrices by the executable.

Boost directly with the simultaneous substitutions in [CONVENTIONS.md](CONVENTIONS.md). At laboratory zero momentum,

\[
\frac{C_{\rm boost}(s,0)}{\gamma^2s^2}
=\gamma(a-bv^2)s+w(1-xv^2).
\]

Both coefficients are positive because `a-bv^2=a(1-yv^2)>0`, including y=1 at any finite boost. The gap is negative. For a putative imaginary-axis root with real transformed variables `(Omega,K)`,

\[
\Re C(i\Omega,K^2)=w(xK^2-\Omega^2),\qquad
\Im C(i\Omega,K^2)=\Omega(bK^2-a\Omega^2).
\]

At nonzero laboratory momentum the real equation implies `Omega^2=xK^2>0`; then the imaginary part is `Omega Gamma K^2`, nonzero. Thus there is no crossing. The boosted cubic leading coefficient is `gamma^3 a(1-yv^2)>0`; bounded normalized coefficients on every closed finite boost interval exclude infinity. Rest RH plus these two direct steps proves all-real-momentum/all-finite-boost spectral stability of this reduced cubic. Its principal factors are `s'(s'^2+yq')`; their speeds follow the all-angle quadratic, with y=0 or the sound y. The shear sector is first-order advection.

Regular paper-F4–F6 with eta=0 and Gamma>0 retain eps1,theta1>0. Apply the quartic proof in Stages 5 and 8 to sound; shear is `s'(theta1 s'+w)`. Its two exact roots are advective `s=-i v kz` and damped `s=-i v kz-w/(gamma theta1)`.

## Vanishing attenuation

For regular finite design parameters, Gamma=0 reduces paper-F1,F2,F4–F6 to `P_N=w^2(s^2+xq)`. Paper-F3 may retain eps1>0, and then

\[
P_N=w(x\varepsilon_1s+w)(s^2+xq).
\]

If eps1=0 it too reduces to ideal sound. The executable checks this retained relaxation factor from the original zero-shear cubic. The ideal wave factor has purely imaginary frequencies for real laboratory momenta, with the all-angle speeds for y=x; its laboratory-zero-momentum quotient is positive `w^2(1-xv^2)`, so it has no relaxation gap. The extra F3 factor has `s=-i v kz-w/(gamma x eps1)`, which is damped. All are spectral statements. Deleted highest-order roots must not be assigned the limiting ratios of absent coefficients.

For the charged map, `Gamma=4eta/3+zeta+script-D T^2 B^2/x`. Nonnegative transport on the regular chart implies eta=zeta=0 and script-D B^2=0. Diffusion can still be positive when B=0; then the original charged determinant is the reduced neutral polynomial times the charge telegrapher and `-Delta_J/w`. This is a permitted boundary, not automatically the completely ideal system.

## Zero diffusion and retained relaxation

For the named prescription `tau_q=alpha_q Dq` with finite alpha_q, script-D=0 implies Dq=tau_q=0 and `F_q=s'`. The charge root is advective; its relaxation gap disappears. With independent tau_q>0 instead, `F_q=s'(1+tau_q s')` retains a gap `-1/(gamma tau_q)` at laboratory zero momentum and roots `-i v kz` and `-i v kz-1/(gamma tau_q)` at general momentum. The two prescriptions have different degree and must have different ledger branches. Three-function shifts preserve the determinant, including these reduced cases, but cannot create a positive shear speed at eta=0.

When every transport vanishes in the regular F6 example, `P_ch=-Delta_J w s(s^2+xq)` has degree three and the full determinant including both first-order shear factors has frequency and total derivative degrees five. The regular positive-transport degrees are instead six and ten. The verifier records these counts explicitly.

## Causal saturation and marginal limits

For y=1 the boosted characteristic equation is `(1-v^2)(c^2-1)=0`. A finite boost never makes the principal frequency coefficient vanish. In the neutral quartic a zero leading q coefficient of a Hurwitz minor does not destroy the positive lower term: with Gamma>0, Delta3 contains the strictly positive `B_L w^3 Gamma q`. Thus the endpoint L=0 can retain strict finite-q damping.

If the leading large-k damping vanishes, continue the asymptotic expansion to its first nonzero real term. Repeated principal roots require a separate dominant balance; do not apply a simple-root derivative formula at a double root. These observations explain why causal saturation is allowed, but they are not a generic certification of every repeated-root matrix. The original evolution pencil's eigenvectors and uniform estimates remain separate obligations.

The singular susceptibility face Delta_J=0 and x=0 or x=1 lie outside the present chart. No continuity claim here extends the construction to those faces.
