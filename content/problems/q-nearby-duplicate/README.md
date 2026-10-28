# Duplicate within k positions

Write `nearby_duplicate(nums, k)` that returns `True` if some value appears twice at
positions at most `k` apart.

```static
nearby_duplicate([1, 2, 3, 1], 3)        ->  True
nearby_duplicate([1, 2, 3, 1, 2, 3], 2)  ->  False
nearby_duplicate([1, 0, 1, 1], 1)        ->  True
```

The point is to practise a dictionary from value to its last position.

## Starter

```python
def nearby_duplicate(nums, k):
    ...
```

## Hints

1. `last = {}` mapping value to the most recent index.
2. For each `i, x`: if `x` is in `last` and `i - last[x] <= k`, return `True`; then set `last[x] = i`.

## Approach

Only the most recent occurrence of each value matters, since it is the closest. One dictionary, one pass.

## Reference

```python
def nearby_duplicate(nums, k):
    last = {}
    for i, x in enumerate(nums):
        if x in last and i - last[x] <= k:
            return True
        last[x] = i
    return False
```
