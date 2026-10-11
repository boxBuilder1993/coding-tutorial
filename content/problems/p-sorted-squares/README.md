# Squares of a sorted list

A sorted list may contain negatives, so squaring the values does not keep
them sorted: `[-3, 1, 2]` squares to `[9, 1, 4]`. The largest square is
always at one of the two ends of the original. Use a position at each end,
compare their squares, write the larger into the **last** free slot of the
result, and move that position inward. Fill the result from the back.

Write `sorted_squares(nums)` that returns a new sorted list of the
squares. The point is to practise filling from both ends rather than call
`sort` or `sorted`.

```static
sorted_squares([-4, -1, 0, 3, 10])  ->  [0, 1, 9, 16, 100]
```

## Starter

```python
def sorted_squares(nums):
    ...
```

## Hints

1. `result = [0] * len(nums)`, `left, right = 0, len(nums) - 1`, and fill position `len(nums) - 1` downwards.
2. `if nums[left] ** 2 > nums[right] ** 2:` take the left one and `left += 1`, else take the right and `right -= 1`.

## Approach

Filling from the back lets you pick the largest remaining square each time, which is always at one end.

## Reference

```python
def sorted_squares(nums):
    n = len(nums)
    result = [0] * n
    left = 0
    right = n - 1
    for fill in range(n - 1, -1, -1):
        if nums[left] ** 2 > nums[right] ** 2:
            result[fill] = nums[left] ** 2
            left += 1
        else:
            result[fill] = nums[right] ** 2
            right -= 1
    return result
```
