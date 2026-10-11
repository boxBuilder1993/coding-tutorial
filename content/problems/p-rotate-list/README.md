# Rotate a list by k

Rotating `[1, 2, 3, 4, 5]` right by 2 gives `[4, 5, 1, 2, 3]`. It can be
done in place with three reversals: reverse the whole list, then reverse
the first `k` items, then reverse the rest. Try it on paper with the
example to see why.

Write `rotate(nums, k)` that rotates the list right by `k` in place and
returns it. `k` may be larger than the list, so reduce it with `%` first.
Do not use slicing to build a new list.

```static
rotate([1, 2, 3, 4, 5], 2)  ->  [4, 5, 1, 2, 3]
rotate([1, 2, 3], 4)        ->  [3, 1, 2]
```

## Starter

```python
def rotate(nums, k):
    ...
```

## Hints

1. Write a helper `reverse(nums, start, end)` that swaps inward between two positions.
2. `k %= len(nums)` (guard the empty list), then `reverse(0, n-1)`, `reverse(0, k-1)`, `reverse(k, n-1)`.

## Approach

The reversal helper is the two-pointer reverse from the earlier page, applied to a range. Three calls do the rotation without extra space.

## Reference

```python
def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1

def rotate(nums, k):
    n = len(nums)
    if n == 0:
        return nums
    k %= n
    reverse(nums, 0, n - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, n - 1)
    return nums
```
