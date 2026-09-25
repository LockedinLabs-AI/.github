"""Check local Markdown links and whitespace in community documents."""
from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1]
failures = []
for path in sorted(root.rglob("*.md")):
    if ".git" in path.parts:
        continue
    text = path.read_text()
    for number, line in enumerate(text.splitlines(), 1):
        if line.rstrip() != line:
            failures.append(f"{path.relative_to(root)}:{number}: trailing whitespace")
    for target in re.findall(r"\]\(([^)]+)\)", text):
        if target.startswith(("https://", "http://", "mailto:", "#")):
            continue
        destination = target.split("#", 1)[0]
        if destination and not (path.parent / destination).exists():
            failures.append(f"{path.relative_to(root)}: missing target {destination}")
if failures:
    print("\n".join(failures))
    sys.exit(1)
print("Community document links and whitespace passed.")
