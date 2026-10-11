"""Generate practice problem folders from a compact spec module (see docstring in README).

Usage: python3 scripts/gen_practice.py path/to/specs.py
Each spec is a dict with slug, title, statement, starter, hints, approach, reference, check.
The generated README.md and check.py are the source of truth; specs are scratch input."""
import importlib, os, sys, textwrap
ROOT = "/home/shravan/Workspaces/coding-tutorial/content/problems"

def write(p):
    d = os.path.join(ROOT, p["slug"])
    os.makedirs(d, exist_ok=True)
    hints = "\n".join(f"{i+1}. {h}" for i, h in enumerate(p["hints"]))
    md = f"""# {p["title"]}

{textwrap.dedent(p["statement"]).strip()}

## Starter

```python
{p["starter"].strip()}
    ...
```

## Hints

{hints}

## Approach

{textwrap.dedent(p["approach"]).strip()}

## Reference

```python
{textwrap.dedent(p["reference"]).strip()}
```
"""
    with open(os.path.join(d, "README.md"), "w") as fh:
        fh.write(md)
    with open(os.path.join(d, "check.py"), "w") as fh:
        fh.write(textwrap.dedent(p["check"]).strip() + "\n")

spec_path = os.path.abspath(sys.argv[1])
sys.path.insert(0, os.path.dirname(spec_path))
mod = importlib.import_module(os.path.splitext(os.path.basename(spec_path))[0])
for p in mod.PROBLEMS:
    write(p)
print(f"wrote {len(mod.PROBLEMS)} problems")
