# Pairs with a difference

Write `pairs_with_difference(nums, k)` that returns how many distinct
pairs of values in `nums` differ by exactly `k`, where `k` is positive.
A pair is a set of two values, so `(1, 3)` and `(3, 1)` are the same
pair, and repeated values count once.

```static
pairs_with_difference([1, 5, 3, 4, 2], 2)  ->  3     (1,3) (3,5) (2,4)
pairs_with_difference([1, 1, 3], 2)        ->  1
pairs_with_difference([1, 2, 3], 5)        ->  0
```

The point is to practise looking up the complement. One check has a
hundred thousand values; the pairwise loop will not finish in time.

## Starter

```python
def pairs_with_difference(nums, k):
    ...
```

## Hints

1. Put the distinct values in a set.
2. For each value `x` in the set, the pair `(x, x + k)` exists if `x + k` is also in the set. Count those.
3. Only check `x + k`, not `x - k`, or every pair is counted twice.

## Approach

`values = set(nums)`, then count the `x` in `values` with `x + k in values`. Each pair is found exactly once, from its smaller member. Linear after the set is built.

## Reference

```python
def pairs_with_difference(nums, k):
    values = set(nums)
    return sum(1 for x in values if x + k in values)
```
