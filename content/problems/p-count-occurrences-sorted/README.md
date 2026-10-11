# Count in a sorted list

In a sorted list, every copy of a value sits together in one block. To
count them without walking the whole list, you can find the block's edges with two
binary searches: one for the first position whose value is at least the
target, and one for the first position whose value is greater than the
target. The count is the difference.

Each search works like this: keep `low` and `high` as the range of
candidate positions, with `high` one past the end. While `low < high`, look
at the middle; if the middle value satisfies the condition ("at least the
target" or "greater than the target"), the answer is at the middle or to
its left, so set `high = mid`; otherwise set `low = mid + 1`. When the loop
ends, `low` is the answer.

Write `count_sorted(sorted_nums, target)` that returns how many times
`target` appears. Do not use `count`.

```static
count_sorted([1, 2, 2, 2, 3, 5], 2)  ->  3
count_sorted([1, 3], 2)              ->  0
```

## Starter

```python
def count_sorted(sorted_nums, target):
    ...
```

## Hints

1. Write a helper `first_at_least(nums, value)` using the described loop, then call it twice: once with `target`, once with `target + 1`.
2. `first_at_least(nums, target + 1) - first_at_least(nums, target)` is the count, since every value between the two edges equals the target.

## Approach

The "first position satisfying a condition" search with `high = mid` is the form that generalises to many problems. Calling it with `target` and `target + 1` brackets the block.

## Reference

```python
def first_at_least(nums, value):
    low = 0
    high = len(nums)
    while low < high:
        mid = (low + high) // 2
        if nums[mid] >= value:
            high = mid
        else:
            low = mid + 1
    return low

def count_sorted(sorted_nums, target):
    return first_at_least(sorted_nums, target + 1) - first_at_least(sorted_nums, target)
```
