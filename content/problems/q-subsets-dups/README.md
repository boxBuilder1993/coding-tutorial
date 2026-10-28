# Subsets with repeated values

Write `unique_subsets(items)` that returns every distinct subset of a list that may
contain repeated values, as a list of lists. Two subsets are the same if they contain the
same values the same number of times. Order of the output does not matter; each subset
should be in non-decreasing order.

```static
unique_subsets([1, 2, 2])  ->  [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
unique_subsets([])         ->  [[]]
```

The point is to practise skipping duplicate choices at the same level after sorting.

## Starter

```python
def unique_subsets(items):
    ...
```

## Hints

1. Sort first. Use the `start` index pattern: `go(start)` records the current partial, then for `i` from `start`, chooses `items[i]` and recurses with `i + 1`.
2. Skip `i` when `i > start` and `items[i] == items[i - 1]`: choosing the second copy at the same level would repeat a subset.

## Approach

Sorting puts duplicates together so the skip rule can see them. Every subset is produced exactly once, in sorted order.

## Reference

```python
def unique_subsets(items):
    items = sorted(items)
    out = []
    partial = []

    def go(start):
        out.append(partial[:])
        for i in range(start, len(items)):
            if i > start and items[i] == items[i - 1]:
                continue
            partial.append(items[i])
            go(i + 1)
            partial.pop()

    go(0)
    return out
```
