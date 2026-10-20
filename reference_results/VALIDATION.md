# Validation record

Completed for supplementary package 1.0.0, 20 October 2026. The frozen manuscript SHA256 is `fcc1dcc2bb2ef0555ce1248dbdcafbe37331ea2763ec9c4f09c55dad4e08a4d8`.

## Outcomes

- **79 exact residual identities passed**, each reducing to exactly zero.
- **49 exact requirements passed**, including thermodynamic and transport domains, design ranges, and polynomial degrees.
- **14 unit tests passed**, including stable/unstable controls, incorrect factorization normalization, an entropy-changing coefficient perturbation, degree reduction, frozen-output protection, and saved failure evidence for negative physical shear viscosity.
- Three rational EOS examples reproduced: a conformal benchmark, a nonconformal unequal-vector frame, and the zero-transport Euler limit. Each stores original matrices/polynomials, actual boosted gap polynomials, and 80-digit root diagnostics with multiplicities and absolute/scaled residuals.
- Exact reference data matched in the isolated archive run. All recorded scaled numerical residuals were below `1e-60` (or exact zero), with matching root multiplicities. This is a diagnostic accuracy check, not a universal stability proof.
- The full nondegenerate neutral determinant has frequency/total derivative degrees 8/8; the charged one has 10/10; the fully ideal charged example has 5/5. The longitudinal Euler example loses its relaxation gaps.
- All 138 manuscript labels and 92 portable Markdown links passed the package integrity check.

See [isolation.log](isolation.log), [environment.json](environment.json), [verification.json](verification.json), [isolated_run.json](isolated_run.json), and [proof_ledger.json](proof_ledger.json) for the actual output and claim scope.

## The five packaging requirements

| Requirement | Implementation and evidence |
|---|---|
| Portable references | Relative links and an anchored source view; labels regenerated from the final copied manuscript; no absolute workspace links in the documentation. |
| Independent AI instructions | Package AGENTS, conventions, verification contract, boundary proofs and templates require no private history, project-state files or old notebooks. |
| Tested dependencies pinned | CPython 3.12.14; SymPy 1.14.0 and mpmath 1.3.0, with universal-wheel hashes in the lock file. No third-party test framework is required. |
| Reference/generated separation | Frozen results and manifest are read-only by workflow; the verifier requires a new directory under generated and rejects reference-directory destinations. New-study templates use a separate generated study. |
| Clean extracted-package test | ZIP extracted to a new temporary location; newly created venv without system site-packages; dependencies installed offline from downloaded wheels with hash enforcement; Python isolated mode; no PYTHONPATH; unrelated working directory. Tests, exact calculations, comparison, scaffolding and frozen-file recheck all passed. |

The isolated dependency inventory confirmed that SymPy and mpmath were loaded from the fresh environment and that the original project was absent from the import path. Temporary filesystem locations in the log are replaced by named placeholders. The release archive excludes all development output, environments, bytecode and filesystem sidecars. Validation records were frozen after execution; the tested calculation code, input data and manuscript hashes remain unchanged in the final archive.

## Source preservation and scope

The parent manuscripts, previous protocol draft, and previous verification script were never written or deleted by this packaging work. During execution the parent manuscript received a title-formatting and author-email change; the package snapshot was refreshed after confirming that the mathematical content was unchanged. [source_refresh.json](source_refresh.json) records the observed source hashes. [original_files_sha256.json](original_files_sha256.json) records the initial preservation baseline; the other tracked files remained byte-identical. The original paper's initial hash differs for the explicitly recorded external update, not a protocol edit.

The package's independent tests replace no historical project certificate. No parent code is imported. The standalone calculations validate selected algebraic identities, not the entire manuscript. Analytic all-momentum/all-boost arguments are conditional results with explicit assumptions in the protocol and boundary document. The stronger local-quadratic ansatz exclusion, new applications, bounded marginal evolution, and nonlinear claims retain their stated unresolved obligations.

Development iterations corrected a generated duplicate keyword before the first successful run and added input/failure-record checks before the final isolated validation. No scientific tolerance was changed to obtain a pass. Old development runs remain in the working package's generated directory and are excluded from the release ZIP.
