# Shortest window with enough

`nums` is a list of positive whole numbers. Write `shortest_window(nums, target)`
that returns the length of the shortest run of consecutive items whose
sum is at least `target`, or `0` if no run reaches it.

```static
shortest_window([2, 3, 1, 2, 4, 3], 7)  ->  2     (4 + 3)
shortest_window([1, 1, 1], 5)           ->  0
shortest_window([5], 5)                 ->  1
```

The point is to practise a variable-size sliding window: grow the right
end until the sum is enough, then shrink from the left while it still is.

## Starter

```python
def shortest_window(nums, target):
    ...
```

## Hints

1. Keep `start`, a running `total`, and `best` (start it at something larger than any answer, like `len(nums) + 1`).
2. For each `end`, add `nums[end]` to `total`. Then `while total >= target`: record `end - start + 1` if smaller, subtract `nums[start]`, move `start` right.
3. If `best` was never updated, return `0`.

## Approach

Both ends only move right, so the loop is linear. The inner `while` shrinks the window as far as it can while still meeting the target, which is where the shortest valid window at each `end` is found. Positive numbers are what make this work: adding an item never decreases the sum, so growing only ever helps.

## Reference

```python
def shortest_window(nums, target):
    best = len(nums) + 1
    total = 0
    start = 0
    for end in range(len(nums)):
        total += nums[end]
        while total >= target:
            best = min(best, end - start + 1)
            total -= nums[start]
            start += 1
    return 0 if best == len(nums) + 1 else best
```
