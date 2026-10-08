# Two Sum

Given a list of integers `nums` and an integer `target`, return the indices
of the two numbers that add up to `target`. Exactly one answer exists, and you
may not use the same element twice. Return the indices in any order.

```static
nums = [2, 7, 11, 15], target = 9  ->  [0, 1]
```

Before coding: the brute force checks every pair. As you scan once, what would
you need to remember about earlier elements?

## Starter

```python
def two_sum(nums: list[int], target: int) -> list[int]:
    """Return indices i, j (i != j) with nums[i] + nums[j] == target."""
    ...
```

## Hints

1. For the current element `x`, you are looking for `target - x` somewhere earlier.
2. Keep a dict mapping value to index for elements already scanned. Check before you insert.

## Approach

One pass with a dict `index_of`. For each `(i, x)`, if `target - x` is in the
dict, return `[index_of[target - x], i]`; otherwise store `index_of[x] = i`.
Checking before inserting means an element is never paired with itself.

Time O(n), space O(n).

## Reference

```python
def two_sum(nums, target):
    index_of = {}
    for i, x in enumerate(nums):
        if target - x in index_of:
            return [index_of[target - x], i]
        index_of[x] = i
    return []
```
