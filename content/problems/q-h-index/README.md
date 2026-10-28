# h-index

A researcher's h-index is the largest `h` such that at least `h` of their papers have
`h` or more citations each. Write `h_index(citations)` for a list of citation counts.

```static
h_index([3, 0, 6, 1, 5])  ->  3     (three papers with at least 3 citations)
h_index([1, 3, 1])        ->  1
h_index([0])              ->  0
```

The point is to practise "sort, then one pass" where the pass compares each value with
its position.

## Starter

```python
def h_index(citations):
    ...
```

## Hints

1. Sort descending. Walking from the top, the `i`-th paper (counting from 1) has at least `i` papers at or above it.
2. The answer is the largest `i` with `sorted_desc[i - 1] >= i`.

## Approach

Sorted descending, position `i` (1-based) has `i` papers with at least that many citations. The h-index is the last position where the citation count is still at least the position. n log n for the sort.

## Reference

```python
def h_index(citations):
    best = 0
    for i, c in enumerate(sorted(citations, reverse=True), start=1):
        if c >= i:
            best = i
        else:
            break
    return best
```
