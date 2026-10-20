# BDNK frame research protocol — supplementary package

Version 1.0.0 · 20 October 2026

A calculation protocol extracted from the supplied final **Stable and causal frames for BDNK hydrodynamics**, by Jay Armas. Begin with [the structure and equation map](docs/RESEARCH_PROTOCOL.md#structure-and-map-to-the-paper), then follow its ten stages. Analyze sector decomposition and shear first; explore alternative longitudinal factorizations before choosing a construction. No application beyond the neutral and single-charge examples is selected or certified.

The package contains the frozen [manuscript source](Paper/BDNKFrames.tex), an [anchored source view](docs/PAPER_SOURCE.html), standalone AI instructions, reusable study templates, exact symbolic checks, rational diagnostic examples, and a proof ledger. Manuscript statements are critically examined rather than presumed independently certified. The source snapshot is for provenance; reproducing the calculations does not require a TeX installation. The paper's embedded style source is preserved byte for byte.

## Run the reference workflow

Use Python 3.12 (tested with CPython 3.12.14). From this extracted folder:

```sh
python3.12 -m venv .venv
.venv/bin/python -m pip install --require-hashes -r requirements-lock.txt
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python scripts/check_package.py
.venv/bin/python scripts/verify_protocol.py
```

On Windows replace `.venv/bin/python` with `.venv\Scripts\python.exe`. Only SymPy 1.14.0 and mpmath 1.3.0 are required; tests use Python's standard-library `unittest`. `requirements.txt` records the same exact pins; `requirements-lock.txt` adds the hashes of the tested universal wheels. Installation needs an index connection or these two wheels in a local wheelhouse. For offline installation use `--no-index --find-links /path/to/wheelhouse` with the lock file. Wheels are not bundled in this source archive.

The verifier can run from any working directory. It writes a new timestamped folder under `generated/`, prints its path, and saves `verification.json`, `paper_labels.json`, and `run.log`. To choose a name, pass an unused absolute or current-working-directory-relative path below this package's `generated/` with `--output`. Existing destinations and paths outside that directory are refused. Failed runs remain available for inspection; success logs are written only after all required checks pass.

To compare a run with the frozen reference:

```sh
.venv/bin/python scripts/compare_reference.py generated/run-REPLACE-WITH-ACTUAL-NAME
```

The comparison checks exact identities, requirements, original matrices and polynomials, degrees, and rational examples. Numerical root ordering and machine metadata may differ; numerical diagnostics are validated separately for residuals, counts and scope. Read [the validation record](reference_results/VALIDATION.md) for actual results and [the ledger](reference_results/proof_ledger.json) for claim limits.

## Start a new research study

Give the next AI [AGENTS.md](AGENTS.md), the [protocol](docs/RESEARCH_PROTOCOL.md), [conventions](docs/CONVENTIONS.md), and [verification requirements](docs/VERIFICATION_REQUIREMENTS.md). Create an unused study directory:

```sh
.venv/bin/python scripts/new_study.py my-system-v1
```

This copies editable templates into `generated/studies/my-system-v1/`. Fill the physical specification and constraint inventory before proposing coefficients. Keep physical transport prescribed. The helper scaffolds evidence; it does not derive or certify a new theory. Record every candidate and rejected factorization in the search table, and attach proofs before advancing ledger entries from unresolved to conditional or established.

## Files and separation of evidence

| Path | Purpose |
|---|---|
| [AGENTS.md](AGENTS.md) | Portable research contract and execution order |
| [docs/RESEARCH_PROTOCOL.md](docs/RESEARCH_PROTOCOL.md) | Ten stages: inputs, calculations, outputs, gates, failures, evidence |
| [docs/BOUNDARY_ANALYSIS.md](docs/BOUNDARY_ANALYSIS.md) | Explicit zero-transport and degree-changing reductions |
| [scripts/verify_protocol.py](scripts/verify_protocol.py) | Original neutral/charged matrices, exact residuals, examples |
| [examples/inputs.json](examples/inputs.json) | Exact rational example parameters |
| [tests/test_verification_methods.py](tests/test_verification_methods.py) | Stable/unstable controls, entropy and remainder failures, boundaries |
| [templates/](templates/) | Problem specification, factor search, claim ledger and proof outline |
| [reference_results/](reference_results/) | Frozen author-generated evidence, source hashes and validation |
| [generated/](generated/) | All new runs and research studies; excluded from release content except its README |
| [MANIFEST.json](MANIFEST.json) | Hashes of all frozen package files except itself |
| [CITATION.cff](CITATION.cff) | Package attribution without an invented DOI |
| [LICENSE_STATUS.md](LICENSE_STATUS.md) | Licensing status; no new license granted by this packaging step |

This package is self-contained with respect to research instructions and calculation code. It does not import the parent project's code, private notes, old searches, chats, or audit files. Reference checks establish selected identities and reproducible examples. Universal all-wavevector/all-boost claims use the explicit conditional proofs in the protocol; neither a PASS nor a numerical scan certifies a new family. Nonlinear causality, strong hyperbolicity, bounded marginal evolution and well-posedness require separate hypotheses and proofs.
