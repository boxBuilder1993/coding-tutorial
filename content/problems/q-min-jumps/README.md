# Fewest jumps to the end

Each position in `jumps` says how far you can jump forward from it, and the end is always
reachable. Write `min_jumps(jumps)` that returns the fewest jumps to get from index 0 to
the last index.

```static
min_jumps([2, 3, 1, 1, 4])  ->  2
min_jumps([1, 1, 1])        ->  2
min_jumps([5])              ->  0
```

The point is to practise greedy in layers: everything reachable with `j` jumps forms a
range, and the next range is the furthest any of those positions can reach.

## Starter

```python
def min_jumps(jumps):
    ...
```

## Hints

1. Keep `end` (the far edge of what the current number of jumps reaches) and `furthest` (the best reach seen while scanning the current range).
2. Scan positions; when you reach `end`, you must jump: `jumps += 1`, `end = furthest`. Stop before the last index.

## Approach

Breadth-first search where each level is a contiguous range, done in one pass with two bookkeeping variables. Linear.

## Reference

```python
def min_jumps(jumps):
    count = 0
    end = furthest = 0
    for i in range(len(jumps) - 1):
        furthest = max(furthest, i + jumps[i])
        if i == end:
            count += 1
            end = furthest
    return count
```
