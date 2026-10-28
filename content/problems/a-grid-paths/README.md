# Paths through a grid

Write `grid_paths(rows, cols)` that returns how many routes go from the
top-left cell to the bottom-right cell of a `rows × cols` grid, moving
only right or down. Both dimensions are at least 1.

```static
grid_paths(1, 1)  ->  1
grid_paths(2, 2)  ->  2
grid_paths(3, 3)  ->  6
grid_paths(3, 7)  ->  28
```

The point is to practise a two-dimensional table. Grids up to `18 × 18`
are checked, where trying every path would take far too long.

## Starter

```python
def grid_paths(rows, cols):
    ...
```

## Hints

1. `table[r][c]` is the number of routes to that cell. The first row and first column are all 1.
2. Every other cell is `table[r - 1][c] + table[r][c - 1]`, filled row by row.
3. Return the bottom-right entry.

## Approach

You reach any cell from the one above or the one to the left, so its count is their sum. Fill the table in reading order so both are ready. Cost `rows × cols`.

## Reference

```python
def grid_paths(rows, cols):
    table = [[1] * cols for _ in range(rows)]
    for r in range(1, rows):
        for c in range(1, cols):
            table[r][c] = table[r - 1][c] + table[r][c - 1]
    return table[rows - 1][cols - 1]
```
