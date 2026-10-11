# Rotate a list by k

Rotating `[1, 2, 3, 4, 5]` right by 2 gives `[4, 5, 1, 2, 3]`. It can be
done in place with three reversals: reverse the whole list, then reverse
the first `k` items, then reverse the rest. On the example, the list goes
`[5, 4, 3, 2, 1]`, then `[4, 5, 3, 2, 1]`, then `[4, 5, 1, 2, 3]`.

Write `rotate(nums, k)` that rotates the list right by `k` in place and
returns it. `k` may be larger than the list; rotating by the length brings
it back to the start, so only `k % len(nums)` matters. The point is to
practise the three reversals rather than build a new list with slicing.

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

1. Write a helper `reverse(nums, start, end)` that swaps the values at `start` and `end` and moves both positions inward until they meet.
2. Guard the empty list, set `k = k % n`, then call `reverse(nums, 0, n - 1)`, `reverse(nums, 0, k - 1)`, and `reverse(nums, k, n - 1)`.

## Approach

The helper is the in-place reverse from the earlier problem, applied to part of the list. Three calls do the rotation without building another list.

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
