# Two sum on a sorted list

When the list is sorted, two positions can find a pair that sums to a
target without checking every pair. Put one position at the start and one
at the end. If the two values add up to the target, you are done. If the
sum is too small, only moving the left position rightwards can make it
bigger; if too large, only moving the right position leftwards can make it
smaller. Repeat until the positions meet.

Write `pair_sum(sorted_nums, target)` that returns the two positions as a
tuple `(left, right)`, or `None` if no pair works. Values are distinct.

```static
pair_sum([1, 3, 4, 6, 8], 10)  ->  (2, 3)
pair_sum([1, 2], 10)           ->  None
```

## Starter

```python
def pair_sum(sorted_nums, target):
    ...
```

## Hints

1. `left, right = 0, len(sorted_nums) - 1` and loop `while left < right`.
2. Compare the sum with the target to decide which pointer moves.

## Approach

Each step rules out one position for good, because the list is sorted. Nested loops also pass the checks; this one teaches the two-pointer form.

## Reference

```python
def pair_sum(sorted_nums, target):
    left = 0
    right = len(sorted_nums) - 1
    while left < right:
        s = sorted_nums[left] + sorted_nums[right]
        if s == target:
            return (left, right)
        if s < target:
            left += 1
        else:
            right -= 1
    return None
```
