# Longest increasing subsequence

Write `lis(nums)` that returns the length of the longest strictly increasing subsequence
(not necessarily adjacent) of `nums`.

```static
lis([10, 9, 2, 5, 3, 7, 101, 18])  ->  4     (2, 3, 7, 101)
lis([7, 7, 7])                     ->  1
lis([])                            ->  0
```

The point is to practise a DP where each subproblem looks back at all earlier ones. The
quadratic version is fine here.

## Starter

```python
def lis(nums):
    ...
```

## Hints

1. `best[i]` = longest increasing subsequence ending at `i`, starting at 1.
2. For each `i`, for each `j < i` with `nums[j] < nums[i]`, `best[i] = max(best[i], best[j] + 1)`. Answer is `max(best)`.
3. There is an n log n version using `bisect` on a list of 'tails'; try it after the quadratic one works.

## Approach

Each position extends the best chain ending at some smaller earlier value. Quadratic; the patience-sorting trick with bisect makes it n log n.

## Reference

```python
def lis(nums):
    if not nums:
        return 0
    best = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                best[i] = max(best[i], best[j] + 1)
    return max(best)
```
