# Split into two equal halves

Write `can_split(nums)` that returns whether the positive whole numbers in `nums` can be
divided into two groups with equal sums.

```static
can_split([1, 5, 11, 5])  ->  True     ([1, 5, 5] and [11])
can_split([1, 2, 3, 5])   ->  False
```

The point is to practise subset-sum DP: which totals can be made from some of the numbers?

## Starter

```python
def can_split(nums):
    ...
```

## Hints

1. If the total is odd, return `False`. The target is `total // 2`.
2. `reachable = {0}`; for each number add `x + n` for every `x` already reachable. Or a boolean list indexed by sum, updated from high to low.
3. Answer: is the target reachable?

## Approach

Subset sum over the possible totals, one number at a time. Set version is simple; the boolean list version is the classic 0/1 knapsack table.

## Reference

```python
def can_split(nums):
    total = sum(nums)
    if total % 2:
        return False
    target = total // 2
    reachable = {0}
    for n in nums:
        reachable |= {x + n for x in reachable if x + n <= target}
    return target in reachable
```
