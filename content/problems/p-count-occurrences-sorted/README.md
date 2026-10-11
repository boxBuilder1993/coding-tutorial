# Count in a sorted list

In a sorted list of whole numbers, every copy of a value sits together in
one block. You can count them without walking the whole list by finding the
two edges of the block.

First, a helper: `first_at_least(nums, value)` returns the first position
whose value is at least `value`, or the length of the list if there is
none. It works like this. Keep `low` and `high` as the range of candidate
positions, with `high` starting one past the end. While `low < high`, look
at the middle position. If the value there is at least `value`, the answer
is at the middle or to its left, so set `high = mid`. Otherwise it must be
to the right, so set `low = mid + 1`. When the loop ends, `low` is the
answer.

Now the count: `first_at_least(nums, target)` is where the block starts,
and `first_at_least(nums, target + 1)` is where it ends, so the count is
the difference. Write `count_sorted(sorted_nums, target)` that returns how
many times `target` appears. The point is to practise the search rather
than call `count`.

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

The "first position where something becomes true" search, with `high = mid`, is the same loop shape many other searches use. Calling it with `target` and `target + 1` finds both ends of the block.

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
