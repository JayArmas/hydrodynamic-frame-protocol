# Conventions and physical inputs

The signature is (-,+,+,+). Fourier amplitudes use `exp(-i omega t+i k.x)`. This package's `s=-i omega` is the paper's `varsigma`; `omega=i s`. Decay means `Re(s)<0`; spectral stability allows equality. Entropy density is `s_ent`. Let `q=|k|^2`; its derivative weight is two, whereas `s` and each momentum component have weight one.

All coefficients in the linear calculation are evaluated at a homogeneous equilibrium `(T0,mu0,u0)`. Equilibrium energy `epsilon` differs from the frame coefficients `eps_i`, code `e1,e2,e3`. `ell` deforms the example EOS; it is not energy or a frame coefficient.

| Symbol | Meaning / code |
|---|---|
| n, w=epsilon+p, r=n/w | Equilibrium density, enthalpy, density ratio |
| alpha=mu/T | Independent thermodynamic coordinate alongside T |
| E,F,N,H | Derivatives epsilon_T at alpha, epsilon_alpha at T, n_T at alpha, n_alpha at T |
| D_J | epsilon_T n_mu - epsilon_mu n_T in the `(T,mu)` chart |
| Delta_J=T D_J=EH-FN | Susceptibility Jacobian in the `(T,alpha)` chart |
| A, TB | Pressure derivatives with respect to epsilon at fixed n, and n at fixed epsilon |
| x=A+rTB | Squared ideal sound speed |
| qT=N-rE, qA=H-rF | Components of the fluctuation `h=delta n-r delta epsilon` |
| Xi=qA-rT^2 qT=T Delta_J x/w | Positive scalar used by the single-charge map |
| eta, zeta, script-D (`Dphys`) | Prescribed nonnegative physical transport |
| Dq=script-D T/Xi | Mode diffusivity, not script-D |
| tau_q | Charge relaxation frame parameter; often alpha_q Dq, but independent on separate boundary branches |
| zeta_* | Auxiliary neutral seed bulk, zeta + script-D T^2 B^2/x |
| Gamma=4eta/3+zeta_* | Neutral seed sound attenuation scale |
| p1,p2,p3; t1,t2,t3; ga1,ga2,ga3 | Code for pi_i, theta_i, gamma_i; gamma_i is not the Lorentz factor |

The charged chart assumes T,w,Delta_J>0 and 0<x<1 plus the fluctuation conditions in [the paper's domain](PAPER_SOURCE.html#app:assumptions). In notation using n_mu at fixed T these include E>=0, n_mu>=0, A+(n_mu/w)T^2 B^2-rTB>=0 and n_mu-n^2/(wx)>=0. Derive these quantities from an EOS. Do not treat arbitrary independent numerical susceptibilities as thermodynamic data.

The original charged matrix has rows energy, longitudinal momentum, charge, and columns `(delta T,delta alpha,delta u_parallel)`. The neutral matrix has rows energy and longitudinal momentum and columns `(delta T/T0,delta u_parallel)`. Normalizations are `P_N=x det(M_N)` and `P_ch=det(M_ch)=-(Delta_J/w) F_q P_N`. Save any alternative row/column normalizations.

For a boost along z, use both arguments simultaneously:

```
s' = gamma (s + i v kz)
q' = kperp^2 + gamma^2 (kz - i v s)^2
gamma = 1/sqrt(1-v^2), |v|<1
```

Complex frequency usually makes transformed momentum complex. At laboratory k=0, `s'=gamma s` and `q'=-gamma^2 v^2 s^2`; a rest-frame k=0 mode cannot simply be relabeled a laboratory gap. Divide the original boosted charged longitudinal determinant by its proved conservation factor `s^3` (and record harmless nonzero gamma normalizations).

Family IDs `paper-F1` through `paper-F6` refer only to this package's frozen source hash. Their classification is not a certificate for differently assigned coefficients. Finite conformal limits mean finite individual coefficients with `eps_i=3pi_i`, `pi1=3pi2`, `nu1=3nu2`, `theta1=theta2`, and `gamma1=gamma2`; divergent coefficients with limiting ratios do not qualify.
