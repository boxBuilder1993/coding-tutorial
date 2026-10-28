# Smallest missing positive

Write `first_missing(nums)` that returns the smallest positive whole number not in the
list. The classic version uses the list itself as the hash table so that extra memory is
constant; a set also passes.

```static
first_missing([1, 2, 0])      ->  3
first_missing([3, 4, -1, 1])  ->  2
first_missing([7, 8, 9])      ->  1
```

The answer is between 1 and `len + 1`. Put each value `v` in that range at index `v - 1`
by swapping, then scan for the first index whose value is wrong.

## Starter

```python
def first_missing(nums):
    ...
```

## Hints

1. Work on a copy. For each `i`, while `1 <= nums[i] <= n` and `nums[nums[i] - 1] != nums[i]`, swap `nums[i]` into its home slot.
2. Afterwards the first `i` with `nums[i] != i + 1` gives `i + 1`; if none, `n + 1`.

## Approach

Cyclic placement: each swap puts one value in its final slot, so total swaps are at most `n`. Linear time, constant extra space.

## Reference

```python
def first_missing(nums):
    nums = list(nums)
    n = len(nums)
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            j = nums[i] - 1
            nums[i], nums[j] = nums[j], nums[i]
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    return n + 1
```
