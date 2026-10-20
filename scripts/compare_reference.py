#!/usr/bin/env python3
"""Compare exact data, separately validating finite numerical diagnostics."""
from pathlib import Path
import argparse
import json
from decimal import Decimal

ROOT=Path(__file__).resolve().parents[1]

def validate_diagnostics(result):
    for example in result["examples"]:
        for sector in ("rest","boosted","gaps"):
            record=example[sector]
            if not record.get("degree"):continue
            assert record["decimal_digits"]==80
            assert sum(r["multiplicity"] for r in record["roots"])==record["degree"]
            for r in record["roots"]:
                assert r["absolute_residual"] and r["root"]
                if r["scaled_residual"]!="exact zero":
                    assert Decimal(r["scaled_residual"])<Decimal("1e-60"), (example["name"],sector,r)

def exact_data(result):
    # Root ordering and platform/Python build strings are not reproducibility targets.
    data={key:value for key,value in result.items() if key not in ("python","platform")}
    for example in data["examples"]:
        for sector in ("rest","boosted","gaps"):
            example[sector].pop("roots",None)
    return data

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run",type=Path)
    args=parser.parse_args()
    reference=json.loads((ROOT/"reference_results/verification.json").read_text())
    result=json.loads((args.run/"verification.json").read_text())
    validate_diagnostics(result)
    validate_diagnostics(reference)
    assert exact_data(result)==exact_data(reference),"Exact reproducibility comparison failed"
    print("PASS: exact reference data match; root multiplicities and 80-digit residual checks pass.")
    print("This is reproducibility of finite diagnostics, not a universal stability proof.")

if __name__=="__main__":main()
