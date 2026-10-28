# k distinct digits with a given sum

Write `digit_combos(k, n)` that returns every combination of `k` distinct digits from 1 to
9 whose sum is `n`, each as an increasing list. Order of the output does not matter.

```static
digit_combos(3, 7)  ->  [[1, 2, 4]]
digit_combos(3, 9)  ->  [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
digit_combos(4, 1)  ->  []
```

The point is to practise two constraints at once, size and sum, each of which can prune.

## Starter

```python
def digit_combos(k, n):
    ...
```

## Hints

1. `go(start, remaining)`: record when `len(partial) == k` and `remaining == 0`.
2. Loop digits from `start` to 9; `break` when the digit exceeds `remaining`; stop early if the partial is already `k` long.

## Approach

Combinations of digits with the sum tracked as the remaining amount. Both constraints prune: too many digits or too large a digit ends the branch.

## Reference

```python
def digit_combos(k, n):
    out = []
    partial = []

    def go(start, remaining):
        if len(partial) == k:
            if remaining == 0:
                out.append(partial[:])
            return
        for d in range(start, 10):
            if d > remaining:
                break
            partial.append(d)
            go(d + 1, remaining - d)
            partial.pop()

    go(1, n)
    return out
```
