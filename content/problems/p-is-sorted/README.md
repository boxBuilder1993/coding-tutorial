# Is it ascending?

Write `is_ascending(nums)` that returns `True` if each number is greater
than or equal to the one before it. Empty and single-item lists count as sorted.

```static
is_ascending([1, 2, 2, 5])  ->  True
is_ascending([3, 1])        ->  False
```

## Starter

```python
def is_ascending(nums):
    ...
```

## Hints

1. Compare each item with its neighbour using `range(len(nums) - 1)`.
2. `if nums[i] > nums[i + 1]: return False`, and `return True` after the loop.

## Approach

One pass comparing neighbours. `nums == sorted(nums)` also works but builds a copy.

## Reference

```python
def is_ascending(nums):
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True
```
