# Cheapest path through a grid

`grid` is a list of lists of non-negative numbers. Write `min_path(grid)` that returns the
smallest sum of values along a path from the top-left to the bottom-right moving only
right or down.

```static
min_path([[1, 3, 1], [1, 5, 1], [4, 2, 1]])  ->  7
min_path([[1, 2], [1, 1]])                   ->  3
```

The point is to practise a 2-D DP with `min` instead of a sum of ways.

## Starter

```python
def min_path(grid):
    ...
```

## Hints

1. First row and column: running sums. Every other cell: its value plus the smaller of the cell above and the cell to the left.
2. You can do it in place on a copy of the grid.

## Approach

Same shape as grid paths with `min` in the recurrence. Rows times columns.

## Reference

```python
def min_path(grid):
    rows, cols = len(grid), len(grid[0])
    table = [row[:] for row in grid]
    for r in range(rows):
        for c in range(cols):
            if r == 0 and c == 0:
                continue
            up = table[r - 1][c] if r > 0 else float("inf")
            left = table[r][c - 1] if c > 0 else float("inf")
            table[r][c] += min(up, left)
    return table[rows - 1][cols - 1]
```
