# Best average over k days

Write `max_average(nums, k)` that returns the largest average of any `k` consecutive
values, as a float. The list has at least `k` values.

```static
max_average([1, 12, -5, -6, 50, 3], 4)  ->  12.75     ((12 - 5 - 6 + 50) / 4)
max_average([5], 1)                     ->  5.0
```

The point is to practise a fixed-size sliding window. One check has a hundred thousand
values with `k` of fifty thousand; recomputing each window's sum will not finish.

## Starter

```python
def max_average(nums, k):
    ...
```

## Hints

1. Sum the first `k`. Then for each later position add the entering value and subtract the leaving one.
2. Track the best sum and divide by `k` at the end.

## Approach

A running window sum updated in constant time per step. Linear.

## Reference

```python
def max_average(nums, k):
    total = sum(nums[:k])
    best = total
    for i in range(k, len(nums)):
        total += nums[i] - nums[i - k]
        best = max(best, total)
    return best / k
```
