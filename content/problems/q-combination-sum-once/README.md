# Combination sum, each number once

Write `combos_once(candidates, target)` that returns every distinct combination of numbers
from `candidates` (which may contain repeats) that sums to `target`, using each position
at most once. Each combination is in non-decreasing order and no combination appears twice.
Order of the output does not matter.

```static
combos_once([10, 1, 2, 7, 6, 1, 5], 8)  ->  [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
combos_once([2, 5, 2, 1, 2], 5)         ->  [[1, 2, 2], [5]]
```

The point is to practise combining the `start + 1` rule (no reuse) with the duplicate
skip at the same level.

## Starter

```python
def combos_once(candidates, target):
    ...
```

## Hints

1. Sort. `go(start, remaining)`; loop `i` from `start`; `break` if the candidate exceeds `remaining`; skip if `i > start` and equal to the previous candidate.
2. Recurse with `i + 1`, not `i`.

## Approach

Sorting enables both the early break and the duplicate skip; recursing with `i + 1` forbids reuse. Each distinct combination appears once.

## Reference

```python
def combos_once(candidates, target):
    candidates = sorted(candidates)
    out = []
    partial = []

    def go(start, remaining):
        if remaining == 0:
            out.append(partial[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remaining:
                break
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            partial.append(candidates[i])
            go(i + 1, remaining - candidates[i])
            partial.pop()

    go(0, target)
    return out
```
