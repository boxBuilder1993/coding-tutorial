# Insertion sort

This is how most people sort a hand of cards. Keep the left part of the
list sorted. Take the next unsorted value, and move it leftwards past every
larger value until it is in the right place among the sorted ones. The
sorted part grows by one each time.

Write `insertion_sort(nums)` that sorts the list in place using this method
and returns it. Do not use `sort` or `sorted`.

```static
insertion_sort([5, 1, 4, 2])  ->  [1, 2, 4, 5]
```

## Starter

```python
def insertion_sort(nums):
    ...
```

## Hints

1. Outer loop from position 1; take `value = nums[i]`; inner `while` shifts larger values right.
2. `j = i - 1; while j >= 0 and nums[j] > value: nums[j + 1] = nums[j]; j -= 1` then `nums[j + 1] = value`.

## Approach

Shifting rather than swapping: larger values move right one slot each, and the taken value drops into the gap.

## Reference

```python
def insertion_sort(nums):
    for i in range(1, len(nums)):
        value = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > value:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = value
    return nums
```
