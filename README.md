# DSA Coding Tutorial

A self-paced, test-driven repo for brushing up on data structures and algorithms.
Each topic has concept notes, a set of problems with hints, a stub you fill in,
a reference solution, and tests that tell you when you got it right.

Zero dependencies: Python 3.10+ and the standard library. Clone and go.

## Quick start

```bash
git clone <this repo> && cd coding-tutorial
make test                       # scoreboard of every problem
make test T=02-arrays-and-hashing          # one topic
make test T=02-arrays-and-hashing/problems/two-sum   # one problem
make test-ref                   # prove the reference solutions pass
make progress                   # regenerate PROGRESS.md
```

No `make`? Every target is a one-line Python command; see the [Makefile](Makefile).

## How to work a problem

1. Read the topic `README.md` first. It explains the pattern, when to reach for it,
   and the template code you will reuse again and again.
2. Open `problems/<slug>/problem.md`. Try the problem for 20 to 30 minutes before
   opening any hint. Hints are collapsed so you will not see them by accident.
3. Write your code in `solution.py`. Run the tests for just that problem.
4. Compare with `reference.py`. Look for differences in approach, not just style.
5. Write the complexity in a comment at the top of your solution. Saying it out
   loud is the part interviews actually test.
6. Come back in a week and redo it from scratch. Spaced repetition beats volume.

## Learning path

Follow the numbered folders in order. Each builds on the previous one.
The full roadmap with suggested pacing is in [CURRICULUM.md](CURRICULUM.md).

| # | Topic | Core idea |
|---|-------|-----------|
| 01 | [Complexity analysis](01-complexity-analysis/) | Big-O, how to reason about time and space |
| 02 | [Arrays and hashing](02-arrays-and-hashing/) | Trade memory for time with hash maps and sets |
| 03 | [Two pointers and sliding window](03-two-pointers-and-sliding-window/) | Linear scans that replace nested loops |
| 04 | [Stacks and queues](04-stacks-and-queues/) | LIFO/FIFO, monotonic stacks |
| 05 | [Linked lists](05-linked-lists/) | Pointer manipulation, dummy heads, fast/slow |
| 06 | [Binary search](06-binary-search/) | Halving a search space, including over answers |
| 07 | [Recursion and backtracking](07-recursion-and-backtracking/) | Choose, explore, un-choose |
| 08 | [Trees](08-trees/) | DFS/BFS, recursion on structure, BSTs |
| 09 | [Heaps and priority queues](09-heaps-and-priority-queues/) | Top-k, k-way merge, scheduling |
| 10 | [Graphs](10-graphs/) | BFS, DFS, topological sort, union-find, shortest paths |
| 11 | [Dynamic programming](11-dynamic-programming/) | Overlapping subproblems, memo to table |
| 12 | [Greedy and intervals](12-greedy-and-intervals/) | Local choice, sort then sweep |
| 13 | [Tries and strings](13-tries-and-strings/) | Prefix trees, string matching |
| 14 | [Bit manipulation](14-bit-manipulation/) | Masks, XOR tricks, bit counting |

## Repo layout

```
dsa_kit/            shared helpers: ListNode/TreeNode converters, test loader
scripts/            run_tests.py (scoreboard + PROGRESS.md), new_problem.py (scaffold)
templates/problem/  files copied by new_problem.py
NN-topic/
  README.md         concept notes, patterns, pitfalls, problem list
  problems/<slug>/
    problem.md      statement, examples, collapsed hints and approach
    solution.py     YOUR code (starts as a stub raising NotImplementedError)
    reference.py    a clean, explained reference solution
    test_solution.py
```

## Using this with a group

- Fork it. Each person works in their own fork so `solution.py` files do not collide.
- Keep `main` as the problem bank. Solutions live in forks or personal branches.
- Run `make progress` and commit `PROGRESS.md` to share where you are.
- Add problems with `make new TOPIC=06-binary-search NAME="Search Insert Position"`.
  See [CONTRIBUTING.md](CONTRIBUTING.md) for the quality bar.
- Pair up: one person solves, the other reviews against the "Before you code"
  checklist in the problem file.

## Resetting a problem

```bash
cp templates/problem/solution.py 02-arrays-and-hashing/problems/two-sum/solution.py
```
Then fix the function signature from `problem.md`. Or just `git checkout` the file.
