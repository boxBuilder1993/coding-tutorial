# Spec: Python Learning Site (MVP)

A single-user, browser-based site for learning Python from zero through
algorithms. The site is a markdown tree. Exercises are a separate library of
problems referenced from that tree. Python runs in the browser with Pyodide.
Hosted on GitHub Pages, no server.

Decided 2026-10-07. Supersedes the earlier draft of this file.

## 1. Content

Two authored formats. Nothing else.

```
content/
  site/                         the markdown tree: navigation and prose
    README.md                   home page
    01-learn-python/
      README.md
      01-values/
        README.md
      02-lists/
        README.md
    02-algorithms/
      README.md
      01-arrays-and-hashing/
        README.md
  problems/                     flat library, one folder per problem
    two-sum/
      README.md
      check.py
    fahrenheit/
      README.md
      check.py
```

### 1.1 Site tree: `content/site/**/README.md`

- A folder is a page. Folders nest without limit. Every folder has a `README.md`.
- Navigation is the directory tree. Display order is the folder name's leading
  numeric prefix; the prefix is stripped for display.
- Page title is the first `#` heading in the README, else the folder name.
- Body is standard markdown (CommonMark plus tables). No frontmatter.
- Every fenced block with info string `python` is runnable in its own sandbox,
  rendered with a Run button and an output area. `python static` renders
  read-only.
- A line `:::problem <id>` embeds the problem `<id>` inline as an exercise card.
- A link whose target is `problem:<id>` opens that problem's standalone page.
- Any other markdown link to a path inside `content/site` navigates within the
  app; external links open normally.

### 1.2 Problems: `content/problems/<id>/`

`README.md`

```markdown
# Two Sum

Given a list of integers `nums` and an integer `target`, return the indices
of the two numbers that add up to `target`. Exactly one answer exists.

```static
nums = [2, 7, 11, 15], target = 9  ->  [0, 1]
```

## Starter

```python
def two_sum(nums: list[int], target: int) -> list[int]:
    """Return indices i, j with nums[i] + nums[j] == target."""
    ...
```

## Hints

1. For the current element x, look for target - x among earlier elements.
2. Keep a dict from value to index. Check it before inserting.

## Approach

One pass with a hash map: check for the complement, then record the element.
Time O(n), space O(n).

## Reference

```python
def two_sum(nums, target):
    index_of = {}
    for i, x in enumerate(nums):
        if target - x in index_of:
            return [index_of[target - x], i]
        index_of[x] = i
    return []
```
```

- `<id>` is the folder name: lowercase kebab-case, unique.
- Title is the first `#` heading.
- Everything before `## Starter` is the statement, shown always. Python fences
  in the statement are runnable like anywhere else.
- `## Starter`: exactly one `python` fence. Prefills the editor. Not runnable in place.
- `## Hints`: ordered list, one hint per item, revealed in order on click. Optional.
- `## Approach`: prose. Hidden until unlocked. Optional.
- `## Reference`: exactly one `python` fence. Hidden until unlocked. Required.
- The four headings are level 2, named exactly as above, in that order. No frontmatter.

`check.py`

```python
from solution import two_sum
from checker import case

case("example", two_sum([2, 7, 11, 15], 9), [0, 1], compare="sorted")
case("negatives", two_sum([-1, -2, -3, -4, -5], -8), [2, 4], compare="sorted")
idx = two_sum([1, 4, 5, 3], 8)
case("does not reuse an element", len(set(idx)), 2)
```

- The learner's editor contents are available as a module named `solution`.
  The checker imports whatever it needs from it. A failed import is reported
  as "your code must define `<name>`".
- `case(name, actual, expected, compare="exact")` records one result.
  `compare` is `exact`, `sorted`, `set`, `approx` (floats, rel 1e-9), or a
  callable `(actual, expected) -> bool`.
- The file runs top to bottom. An uncaught exception records a failed case
  named for the line where it happened and stops checking.
  `NotImplementedError` raised from `solution` is reported as "not attempted".
- `checker` also exports `ListNode`, `TreeNode`, `from_list`, `to_list`,
  `from_level_order`, `to_level_order` for linked-list and tree problems.
- Checkers must finish within the run time budget (§2). Keep inputs modest.
- The same file runs under CPython in the build, with the Reference block as
  `solution`, and under Pyodide in the browser with the learner's code.

## 2. Execution

- Every run is a fresh sandbox: new globals, no state from any earlier run,
  block, or exercise. This is a rule, not a default.
- Play block: the fence text runs as a script. All of `stdout` and `stderr`
  is captured and shown, in order, including output produced before an
  exception. Expression values are never echoed; output comes only from
  `print`. Lessons introduce `print` before anything else.
- Exercise run: the editor text is registered as module `solution`, then
  `check.py` executes. Results are a list of `{name, status, expected, actual, message}`.
- `input()` is unsupported. Content must not use it.
- Pyodide runs in a Web Worker. Messages: `run {code}`, `test {code, checkSource}`,
  `stop`. `stop` terminates and restarts the worker.
- Time budget per run: 10 seconds, then "timed out".
- Recursion limit in the sandbox: 10,000.

## 3. Website

Routes, hash-based.

| Route | Page |
|-------|------|
| `#/` | `content/site/README.md` |
| `#/<path>` | The site page at `content/site/<path>/README.md`, e.g. `#/01-learn-python/02-lists` |
| `#/problem/<id>` | Standalone problem page |
| `#/problems` | Generated list of every problem in the library, with solved status |
| `#/settings` | Export, import, reset progress |

Layout

- Left sidebar renders the site tree. Groups collapse. Leaves show a status
  icon: a page is done when every problem embedded in it is solved; pages with
  no problems show no status. Drawer on narrow screens.
- Site page: rendered markdown in one column. Play blocks show code, Run,
  output. Each `:::problem` renders an exercise card.
- Problem page: statement left, editor and results right, draggable divider.
- Exercise card: statement with Hints collapsed, editor prefilled with Starter,
  Run tests, results list, Reset to starter. Each card is independent.

Hints and reveal

- Hints unlock one at a time by click; the count is stored.
- Approach and Reference unlock when all cases pass, or when every hint has
  been used and the learner clicks "Show approach". Reveal is stored.
- Problem status: `not-started`, `in-progress` (edited or run), `solved`.
  "Solved with help" is derived from `hintsUsed > 0 || revealed`.

Results and errors

- Per case: name, pass or fail, and on failure expected and actual on
  separate lines.
- Python errors show a one-line plain-language summary first (syntax error
  with line, undefined name, type error, timeout, missing definition), with
  the raw traceback collapsed below.

Editor

- CodeMirror 6, Python mode, line numbers, bracket matching, 4-space indent,
  Tab inserts spaces. No autocomplete. Ctrl/Cmd+Enter runs.
- Autosave to local storage on change, debounced.

Loading

- Markdown renders immediately. Pyodide loads in the background from the
  jsdelivr CDN at a pinned version; Run buttons show a spinner until ready. First load is several MB, cached
  by the browser afterwards.

## 4. Progress

`localStorage` key `pyl.progress.v1`:

```json
{
  "version": 1,
  "lastRoute": "#/01-learn-python/02-lists",
  "problems": {
    "two-sum": {
      "status": "not-started|in-progress|solved",
      "code": "<latest editor contents>",
      "hintsUsed": 0,
      "revealed": false,
      "firstSolved": "<iso>|null",
      "attempts": 0
    }
  }
}
```

- Keyed by problem id only. Reorganising the site tree never affects progress.
- Export downloads this JSON. Import replaces it after confirmation. Reset
  clears it after confirmation.

## 5. Build and deploy

`scripts/build_content.py`, CPython, standard library only.

1. Walk `content/site`; emit the tree with paths, titles, and the problem ids
   each page embeds.
2. Walk `content/problems`; validate each README has the required headings
   and exactly one fence under Starter and Reference; record titles.
3. Verify every `:::problem` and `problem:` reference resolves. Warn on
   problems referenced from nowhere.
4. For each problem, load the Reference block as `solution` and run `check.py`.
   Any failed case fails the build.
5. Emit `site/public/content/tree.json` and `site/public/content/problems.json`,
   and copy `content/` into `site/public/content/` so the app fetches markdown
   and checkers as static files.

GitHub Actions on push to `main`: run the build script, build the Vite app,
deploy `site/dist` to Pages. Vite `base` is the repository path. A failing
content build blocks deployment.

## 6. App stack

React, TypeScript, Vite. CodeMirror 6. react-markdown with custom renderers
for `python` fences, `:::problem` lines, and `problem:` links. Pyodide in a
Web Worker. No state library beyond React context.

## 7. MVP scope

- All routes in §3, sidebar from the tree, progress storage, export and import.
- Runner with sandboxing, play blocks, checker API, stop, timeout, error summaries.
- Content: one beginner module of about five pages with embedded problems,
  and roughly ten algorithm problems converted from the earlier draft.
- Build script and Pages workflow.

Deferred: difficulty and tags, prerequisites, filters on the problems page,
review and spaced repetition, theming beyond light and dark, the full curriculum.

## 8. Decisions on earlier open questions

- Play blocks never echo expression values. Output is only what `print` writes.
- Pyodide is loaded from the CDN at a pinned version. Self-hosting is deferred
  unless CDN dependence becomes a problem.
