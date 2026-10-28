# Largest product of a run

Write `max_product(nums)` that returns the largest product of any non-empty run of
consecutive items. Values may be negative or zero.

```static
max_product([2, 3, -2, 4])    ->  6
max_product([-2, 0, -1])      ->  0
max_product([-2, 3, -4])      ->  24
```

Track both the largest and the smallest product of a run ending at each position: a
negative number turns the smallest into the largest.

## Starter

```python
def max_product(nums):
    ...
```

## Hints

1. Keep `hi` and `lo`, the max and min product of a run ending here, both starting at the first item.
2. For each next `x`, the candidates are `x`, `hi * x`, `lo * x`; new `hi` is their max and new `lo` their min. Track the best `hi` seen.

## Approach

Kadane's idea extended with a running minimum, because multiplying by a negative swaps the extremes. Linear.

## Reference

```python
def max_product(nums):
    hi = lo = best = nums[0]
    for x in nums[1:]:
        candidates = (x, hi * x, lo * x)
        hi, lo = max(candidates), min(candidates)
        best = max(best, hi)
    return best
```
