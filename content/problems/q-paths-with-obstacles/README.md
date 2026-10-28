# Grid paths around obstacles

`grid` is a list of lists of `0` (open) and `1` (blocked). Write `paths(grid)` that
returns how many routes go from the top-left to the bottom-right moving only right or
down, never entering a blocked cell. If either corner is blocked the answer is 0.

```static
paths([[0, 0, 0], [0, 1, 0], [0, 0, 0]])  ->  2
paths([[0, 1], [0, 0]])                   ->  1
paths([[1]])                              ->  0
```

The point is to practise a 2-D table where some cells are forced to zero.

## Starter

```python
def paths(grid):
    ...
```

## Hints

1. `table[r][c]` is 0 for a blocked cell; otherwise the sum of the cell above and the cell to the left (treat outside as 0).
2. Seed `table[0][0] = 1` unless blocked.

## Approach

The usual grid-paths recurrence with obstacles contributing zero routes. Rows times columns.

## Reference

```python
def paths(grid):
    rows, cols = len(grid), len(grid[0])
    table = [[0] * cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                continue
            if r == 0 and c == 0:
                table[r][c] = 1
            else:
                table[r][c] = (table[r - 1][c] if r > 0 else 0) + (table[r][c - 1] if c > 0 else 0)
    return table[rows - 1][cols - 1]
```
