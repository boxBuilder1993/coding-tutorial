# Choose k from n

Write `combinations(n, k)` that returns every way to choose `k` distinct numbers from
`1` to `n`, each as an increasing list. Order of the output does not matter.

```static
combinations(4, 2)  ->  [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
combinations(3, 3)  ->  [[1, 2, 3]]
combinations(3, 0)  ->  [[]]
```

The point is to practise the `start` index pattern with a size limit, and pruning when
too few numbers remain.

## Starter

```python
def combinations(n, k):
    ...
```

## Hints

1. `go(start)`: if `len(partial) == k`, record. Otherwise for `i` from `start` to `n`, append `i`, recurse with `i + 1`, pop.
2. Prune: stop the loop when `n - i + 1 < k - len(partial)`, since not enough numbers remain to fill the combination.

## Approach

Choosing in increasing order prevents repeats; the remaining-count prune avoids dead branches. Output size is n choose k.

## Reference

```python
def combinations(n, k):
    out = []
    partial = []

    def go(start):
        if len(partial) == k:
            out.append(partial[:])
            return
        for i in range(start, n + 1):
            if n - i + 1 < k - len(partial):
                break
            partial.append(i)
            go(i + 1)
            partial.pop()

    go(1)
    return out
```
