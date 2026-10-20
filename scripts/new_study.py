#!/usr/bin/env python3
"""Copy editable research templates to a new, versioned local study."""
from pathlib import Path
import argparse
import re
import shutil

ROOT=Path(__file__).resolve().parents[1]

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("study_id",help="Lowercase letters, digits, underscores and hyphens, ending in a version")
    args=parser.parse_args()
    if not re.fullmatch(r"[a-z][a-z0-9_-]{0,95}",args.study_id):parser.error("Use a simple lowercase study identifier")
    target=ROOT/"generated/studies"/args.study_id
    target.mkdir(parents=True,exist_ok=False)
    for source in (ROOT/"templates").iterdir():
        if source.is_file() and not source.name.startswith("._"):shutil.copyfile(source,target/source.name)
    print("Created study:",target)
    print("Fill the specification and derive original equations before proposing frames.")

if __name__=="__main__":main()
