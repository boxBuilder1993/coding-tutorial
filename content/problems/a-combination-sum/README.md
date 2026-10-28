# Combination sum

Write `combination_sum(candidates, target)` that returns every
combination of the distinct positive `candidates` that adds up to
`target`, where each candidate may be used any number of times. Each
combination is a list in non-decreasing order, and no combination appears
twice. Order of the results does not matter.

```static
combination_sum([2, 3, 6, 7], 7)  ->  [[2, 2, 3], [7]]
combination_sum([2, 3, 5], 8)     ->  [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
combination_sum([2], 1)           ->  []
```

The point is to practise pruning and the `start` index that stops the
same combination appearing in different orders.

## Starter

```python
def combination_sum(candidates, target):
    ...
```

## Hints

1. Sort the candidates. Inner function `go(start, remaining)`: when `remaining == 0`, record a copy.
2. Loop `i` from `start`; `break` when `candidates[i] > remaining` (sorted, so nothing later fits either).
3. Append, call `go(i, remaining - candidates[i])` (same `i`, since reuse is allowed), pop.

## Approach

Choices at each level are the candidates from `start` onwards, so later levels never pick a smaller candidate than an earlier one and every combination is produced once, in sorted order. Sorting plus the `break` prunes whole branches.

## Reference

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
```
