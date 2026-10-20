#!/usr/bin/env python3
"""Check the frozen package manifest, relative links, and source-label map."""
from pathlib import Path
import hashlib
import json
import re
from urllib.parse import unquote, urlsplit

ROOT=Path(__file__).resolve().parents[1]

def included(path):
    rel=path.relative_to(ROOT)
    if rel.as_posix()=="MANIFEST.json":return False
    if any(part.startswith("._") or part in (".venv","__pycache__") for part in rel.parts):return False
    return rel.parts[0]!="generated" or rel.as_posix()=="generated/README.md"

def main():
    manifest=json.loads((ROOT/"MANIFEST.json").read_text())
    expected=manifest["sha256"]
    actual={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest()
            for p in ROOT.rglob("*") if p.is_file() and included(p)}
    if actual!=expected:
        changed=sorted(set(actual)^set(expected) | {p for p in actual.keys()&expected.keys() if actual[p]!=expected[p]})
        raise AssertionError("Frozen files differ from manifest: "+", ".join(changed))
    labels={label:i for i,line in enumerate((ROOT/"Paper/BDNKFrames.tex").read_text().splitlines(),1)
            for label in re.findall(r"\\label\{([^}]+)\}",line)}
    assert labels==json.loads((ROOT/"reference_results/paper_labels.json").read_text())
    html=(ROOT/"docs/PAPER_SOURCE.html").read_text()
    assert all(f'id="{label}"' in html for label in labels)
    evidence=json.loads((ROOT/"reference_results/verification.json").read_text())
    claims=json.loads((ROOT/"reference_results/proof_ledger.json").read_text())["claims"]
    ids={c["claim_id"] for c in claims}
    for claim in claims:
        assert claim["status"] in ("established_identity","conditional_result","conjecture","unresolved_gap")
        assert set(claim["exact_checks"]) <= evidence["checks"].keys(),claim["claim_id"]
        assert set(claim["depends_on"]) <= ids,claim["claim_id"]
        if claim["analytic_proof"]:
            assert (ROOT/claim["analytic_proof"].split("#")[0]).exists(),claim["claim_id"]
    links=0
    for source in ROOT.rglob("*.md"):
        if not included(source):continue
        text=source.read_text()
        assert "/Volumes/" not in text and "/Users/" not in text, source
        for destination in re.findall(r"\[[^\]\n]+\]\(([^)\n]+)\)",text):
            target=urlsplit(destination.strip("<>"))
            if target.scheme or target.netloc:continue
            assert not target.path.startswith("/"),(source,destination)
            path=(source.parent/unquote(target.path)).resolve()
            assert path==ROOT or ROOT in path.parents,(source,destination)
            assert path.exists(),(source,destination)
            if target.fragment:
                data=path.read_text()
                if path.suffix==".html":
                    assert f'id="{unquote(target.fragment)}"' in data,(source,destination)
                elif path.suffix==".md":
                    headings=[re.sub(r"[^\w -]","",h.lower()).replace(" ","-") for h in re.findall(r"^#+ (.+)$",data,re.M)]
                    assert target.fragment in headings,(source,destination)
            links+=1
    print(f"PASS: {len(actual)} frozen file hashes; {len(labels)} manuscript labels; {links} portable links.")

if __name__=="__main__":main()
