---
title: Backtracking in Python: subsets, permutations, combination sum and N-queens
description: Build candidates one choice at a time, undo and try the next: subsets, permutations, combination sum with pruning, and the N-queens count.
---
# Backtracking

Some problems have no shortcut: you have to look at every arrangement.
All subsets of a set, every ordering of a list, every way to place pieces
on a board. **Backtracking** is the disciplined way to enumerate them:
make a choice, recurse to fill in the rest, then **undo** the choice and
try the next one. The undo is what distinguishes it from plain recursion,
and the ability to give up early on a partial arrangement that cannot
work, called pruning, is what makes it usable.

## The template

```python static
def backtrack(partial):
    if partial is complete:
        record a copy of partial
        return
    for each choice available at this point:
        add choice to partial
        backtrack(partial)
        remove choice from partial
```

`partial` is a single list reused throughout, which is why the result must
be copied when recorded and why every add has a matching remove.

## Subsets

Every subset of `[1, 2, 3]`. At each index decide: include it or not.

```python
def subsets(items):
    out = []
    partial = []

    def go(i):
        if i == len(items):
            out.append(partial[:])
            return
        go(i + 1)
        partial.append(items[i])
        go(i + 1)
        partial.pop()

    go(0)
    return out

print(subsets([1, 2, 3]))
```

Two branches per item, so `2**n` subsets, and each is recorded in the
order the choices are made. `partial[:]` makes the copy; appending
`partial` itself would record one list that keeps changing. The inner
function `go` can see `items`, `out` and `partial` from the enclosing one,
which saves passing them along on every call.

## Permutations

Every ordering. Pick each unused item for the next slot:

```python
def permutations(items):
    out = []
    partial = []
    used = [False] * len(items)

    def go():
        if len(partial) == len(items):
            out.append(partial[:])
            return
        for i in range(len(items)):
            if used[i]:
                continue
            used[i] = True
            partial.append(items[i])
            go()
            partial.pop()
            used[i] = False

    go()
    return out

print(permutations([1, 2, 3]))
print(len(permutations([1, 2, 3, 4, 5])))
```

The `used` list is the state alongside `partial`, and both are undone
after the recursive call. `n!` orderings, which is 120 for five items and
3.6 million for ten; backtracking cannot make an exponential problem
small, only avoid wasted work within it.

## Pruning: combination sum

Which combinations of the candidate numbers add up to a target, each
candidate usable many times? Without pruning you would build every
combination and check. With it, stop as soon as the running total passes
the target, and start each level at the current index so `[2, 3]` and
`[3, 2]` are not both produced.

```python
def combination_sum(candidates, target):
    out = []
    partial = []
    candidates = sorted(candidates)

    def go(start, remaining):
        if remaining == 0:
            out.append(partial[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remaining:
                break
            partial.append(candidates[i])
            go(i, remaining - candidates[i])
            partial.pop()

    go(0, target)
    return out

print(combination_sum([2, 3, 6, 7], 7))
print(combination_sum([2, 3, 5], 8))
```

Sorting first lets the `break` cut off every larger candidate at once.
Passing `i` rather than `i + 1` allows reuse; `i + 1` would give
combinations without repetition. The `start` parameter is the standard way
to generate combinations rather than permutations.

## N-queens

Place `n` queens on an `n × n` board so none attacks another. Place one
queen per row, trying each column, and prune any column or diagonal
already attacked.

```python
def n_queens(n):
    count = 0
    cols = set()
    diag1 = set()
    diag2 = set()

    def go(row):
        nonlocal count
        if row == n:
            count += 1
            return
        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue
            cols.add(col); diag1.add(row - col); diag2.add(row + col)
            go(row + 1)
            cols.remove(col); diag1.remove(row - col); diag2.remove(row + col)

    go(0)
    return count

print([n_queens(n) for n in range(1, 9)])
```

The two diagonals through a cell are identified by `row - col` and
`row + col`, which are constant along them. Three sets answer "is this
square attacked" in constant time, and pruning at the first conflict is
what makes `n = 8` finish instantly despite `8**8` possible placements.
`nonlocal count` lets the inner function change the outer one's variable;
a one-element list or returning counts would do the same.

## When to backtrack

- The answer is **all** arrangements, or the **count** of them, or you must
  find **one** satisfying hard constraints (Sudoku, word search, puzzles).
- The input is small, under about twenty items, because the output itself
  is exponential.
- If the question asks for the best value rather than the arrangements,
  and subproblems overlap, it is dynamic programming instead. If a safe
  local choice exists, it is greedy. Backtracking is the last resort, and
  the right one when the others do not apply.

## Try it

Where the exercise returns a list of lists, the checker compares the
collection regardless of the order you produce it in.

:::problem a-subsets

:::problem a-permutations

:::problem a-combination-sum

:::problem a-n-queens

Next: [Algorithms practice](../14-practice), 112 problems grouped by topic.
