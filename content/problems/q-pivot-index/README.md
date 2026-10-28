# Balance point

Write `pivot_index(nums)` that returns the smallest index where the sum of everything to
its left equals the sum of everything to its right, or `-1` if there is none. The ends
count as having an empty side summing to 0.

```static
pivot_index([1, 7, 3, 6, 5, 6])  ->  3
pivot_index([1, 2, 3])           ->  -1
pivot_index([2, 1, -1])          ->  0
```

The point is to practise a running left sum against a known total instead of two prefix lists.

## Starter

```python
def pivot_index(nums):
    ...
```

## Hints

1. `total = sum(nums)`, `left = 0`. For each index, the right sum is `total - left - nums[i]`.
2. Return the first index where `left == right`; add `nums[i]` to `left` afterwards.

## Approach

One pass with the total precomputed: the right side is total minus left minus the pivot. Linear, constant extra space.

## Reference

```python
def pivot_index(nums):
    total = sum(nums)
    left = 0
    for i, x in enumerate(nums):
        if left == total - left - x:
            return i
        left += x
    return -1
```
