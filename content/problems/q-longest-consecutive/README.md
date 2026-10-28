# Longest run of consecutive values

Write `longest_consecutive(nums)` that returns the length of the longest sequence of
consecutive whole numbers that all appear in `nums`, in any order and with repeats allowed.

```static
longest_consecutive([100, 4, 200, 1, 3, 2])  ->  4     (1, 2, 3, 4)
longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])  ->  9
longest_consecutive([])  ->  0
```

The point is to practise a set that lets you start counting only at the beginning of a
run. Sorting also works; the set version is linear.

## Starter

```python
def longest_consecutive(nums):
    ...
```

## Hints

1. Put everything in a set. A value `x` starts a run only if `x - 1` is not in the set.
2. From each start, count upwards while `x + 1, x + 2, ...` are in the set. Each value is counted in exactly one run.

## Approach

Only run starts trigger counting, and each value is walked over once in total, so the whole thing is linear despite the inner loop.

## Reference

```python
def longest_consecutive(nums):
    values = set(nums)
    best = 0
    for x in values:
        if x - 1 in values:
            continue
        length = 1
        while x + length in values:
            length += 1
        best = max(best, length)
    return best
```
