# Largest island

`grid` is a list of strings of `1` (land) and `0` (water). Write `max_island(grid)` that
returns the number of cells in the largest island (cells connected up, down, left or
right), or `0` if there is no land.

```static
max_island(["110", "010", "001"])  ->  3
max_island(["000"])                ->  0
```

The point is to practise measuring each component rather than just counting them.

## Starter

```python
def max_island(grid):
    ...
```

## Hints

1. Same flood as counting islands, but count the cells each flood visits.
2. Keep the maximum.

## Approach

Connected components with a size per component. Linear in cells.

## Reference

```python
def max_island(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    seen = set()
    best = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "1" or (r, c) in seen:
                continue
            size = 0
            stack = [(r, c)]
            while stack:
                x, y = stack.pop()
                if (x, y) in seen or not (0 <= x < rows and 0 <= y < cols) or grid[x][y] != "1":
                    continue
                seen.add((x, y))
                size += 1
                stack.extend([(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)])
            best = max(best, size)
    return best
```
