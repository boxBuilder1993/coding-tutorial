# Split into k pieces, minimise the largest

Write `min_largest_sum(nums, k)` that splits the non-negative list into `k` non-empty
consecutive pieces so that the largest piece sum is as small as possible, and returns
that sum.

```static
min_largest_sum([7, 2, 5, 10, 8], 2)  ->  18
min_largest_sum([1, 2, 3, 4, 5], 2)   ->  9
min_largest_sum([1, 4, 4], 3)         ->  4
```

Binary search on the answer: for a candidate maximum, greedily count how many pieces are
needed; if at most `k`, the candidate is achievable.

## Starter

```python
def min_largest_sum(nums, k):
    ...
```

## Hints

1. `pieces(limit)`: walk the list, starting a new piece whenever adding the next item would exceed `limit`; return the piece count.
2. Search `limit` from `max(nums)` to `sum(nums)` for the smallest with `pieces(limit) <= k`.

## Approach

A limit either works or does not and larger limits always work if smaller do, so binary search over limits with a linear greedy check.

## Reference

```python
def min_largest_sum(nums, k):
    def pieces(limit):
        count, load = 1, 0
        for x in nums:
            if load + x > limit:
                count += 1
                load = 0
            load += x
        return count

    low, high = max(nums), sum(nums)
    while low < high:
        mid = (low + high) // 2
        if pieces(mid) <= k:
            high = mid
        else:
            low = mid + 1
    return low
```
