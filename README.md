# Learn Python

A browser-based, self-paced course that teaches Python from zero: four
modules of lessons with runnable examples and exercises, then 120 practice
problems. Python runs in the browser via Pyodide, so learners install
nothing. Live at https://boxbuilder1993.github.io/coding-tutorial/

The design is in [SPEC.md](SPEC.md). In short: the site is a markdown tree,
exercises are a library of problems each with a Python checker, and every
runnable code block is its own sandbox.

## Layout

```
content/site/**/README.md      site pages; folder = page, numeric prefix = order
content/problems/<id>/          README.md (statement, Starter, Hints, Approach, Reference) + check.py
site/                          React + Vite app; e2e/ holds the Playwright tests
site/runner/checker.py         the `case` API used by every check.py
scripts/build_content.py       validates content, verifies references, emits site/public/content/
scripts/gen_practice.py        generates problem folders from a compact spec module
.github/workflows/pages.yml    checks, builds and deploys to GitHub Pages on push to main
Makefile                       the entry point for all of the below
```

## Checks

`make check` runs everything CI runs:

1. Content validation. Every page and problem is parsed, every reference
   solution is run against its `check.py` under CPython, and every
   `:::problem` reference must resolve.
2. TypeScript typecheck and production build. The build pre-renders an
   `index.html` for every page and problem (`site/scripts/prerender.mjs`),
   with title, description, canonical and Open Graph tags and the page text
   in the body, plus `sitemap.xml`, `robots.txt` and `404.html`. Search
   engines and link previews see complete pages; the app takes over on load.
   `SITE_URL` sets the absolute site address used in canonical links and the
   sitemap (CI sets it from the repository name).
3. Playwright smoke tests: loading, running a block, solving an exercise,
   error messages, the time budget, search, the tutor prompt, dark mode,
   path routing and the redirect of old `#/` links.
4. A content sweep that visits every page in a real browser, runs every code
   block, submits every reference solution to its exercise, and follows every
   internal link. A block that is meant to error is tagged
   ```` ```python expect-error ```` and the sweep checks that it does. The
   sweep writes a report to `review/sweep.md`.
5. Pre-render checks that load the built pages with JavaScript disabled and
   assert the text, title, description and canonical link are present, and
   that the sitemap lists every URL exactly once in path form.

```bash
make check     # all of the above
make test      # smoke tests only
make sweep     # content sweep only
make content   # content validation only
```

Playwright starts the dev server and the preview server itself. To run the
browser checks against the live site instead:
`E2E_BASE_URL=https://boxbuilder1993.github.io/coding-tutorial/ npx playwright test` from `site/`.

URLs are path-based (`/01-learn-python/02-decisions-and-text/`); every page
has a real file behind it. Old `#/...` links redirect in the browser.

## Local development

Requires Python 3.10+ and Node 20+. First time: `cd site && npx playwright install chromium`.

```bash
make dev       # validates content, then serves http://localhost:5173
```

Re-run `make content` after editing content; the dev server serves its output.
If the server stops seeing new content after a rebuild, restart it.

## Writing content

- A page is a folder with a `README.md` under `content/site`. The numeric
  prefix orders it; the first `#` heading is its title. Every ```` ```python ````
  fence is runnable; ```` ```python static ```` is read-only; ```` ```python expect-error ````
  is runnable and expected to fail.
- A problem is `content/problems/<id>/README.md` with the level-2 headings
  `Starter`, `Hints`, `Approach`, `Reference` in that order, plus a `check.py`
  that imports from `solution` and calls `case(...)`. Embed it in a page with
  a line `:::problem <id>`, or link to it with `[text](problem:<id>)`.
- The build fails if a reference solution does not pass its own checker, and
  `make check` fails if it does not pass in the browser either.
