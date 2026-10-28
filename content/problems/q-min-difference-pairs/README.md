# Pairs with the smallest difference

`items` is a list of at least two distinct whole numbers. Write `closest_pairs(items)`
that returns every pair `[a, b]` with `a < b` whose difference is the smallest difference
between any two values, ordered by `a`.

```static
closest_pairs([4, 2, 1, 3])      ->  [[1, 2], [2, 3], [3, 4]]
closest_pairs([1, 3, 6, 10, 15]) ->  [[1, 3]]
```

The point is to practise "sort first": once sorted, the closest pairs are neighbours.

## Starter

```python
def closest_pairs(items):
    ...
```

## Hints

1. Sort. The minimum difference is the smallest gap between neighbours.
2. Second pass over the neighbours collecting those with that gap.

## Approach

After sorting, only adjacent values can be the closest. Two linear passes: find the minimum gap, then collect the pairs with it.

## Reference

```python
def closest_pairs(items):
    s = sorted(items)
    gap = min(s[i + 1] - s[i] for i in range(len(s) - 1))
    return [[s[i], s[i + 1]] for i in range(len(s) - 1) if s[i + 1] - s[i] == gap]
```
