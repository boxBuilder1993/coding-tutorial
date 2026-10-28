# Split into k equal groups

Write `can_partition(nums, k)` that returns whether the positive whole numbers can be
divided into `k` non-empty groups with equal sums.

```static
can_partition([4, 3, 2, 3, 5, 2, 1], 4)  ->  True     (5), (1,4), (2,3), (2,3)
can_partition([1, 2, 3, 4], 3)           ->  False
```

Backtracking with `k` buckets: place each number (largest first) into a bucket that still
has room, undo on failure. Skip buckets with the same current total as one already tried.

## Starter

```python
def can_partition(nums, k):
    ...
```

## Hints

1. Total must divide by `k`; target is `total // k`; any number above the target means `False`. Sort descending so big numbers are placed first.
2. `go(i)`: if `i == len(nums)` return `True`. For each bucket with `bucket + nums[i] <= target`, add, recurse, remove.
3. Prune: if two buckets have the same total, trying the second is pointless; and if a bucket is empty and placing fails, no other empty bucket will work either.

## Approach

Search over bucket assignments with strong pruning: descending order fails fast, and equal-bucket skipping removes symmetric branches.

## Reference

```python
def can_partition(nums, k):
    total = sum(nums)
    if k == 0 or total % k:
        return False
    target = total // k
    nums = sorted(nums, reverse=True)
    if nums and nums[0] > target:
        return False
    buckets = [0] * k

    def go(i):
        if i == len(nums):
            return True
        seen = set()
        for b in range(k):
            if buckets[b] + nums[i] > target or buckets[b] in seen:
                continue
            seen.add(buckets[b])
            buckets[b] += nums[i]
            if go(i + 1):
                return True
            buckets[b] -= nums[i]
            if buckets[b] == 0:
                break
        return False

    return go(0)
```
