# Shelf totals

`grid` is a list of rows, each row a list of quantities on one shelf. Write
`shelf_report(grid)` that returns a dictionary with three entries: `"rows"`,
a list of each row's total; `"columns"`, a list of each column's total;
and `"max_row"`, the index of the row with the largest total (first on ties).
The grid has at least one row and all rows have the same length.

```static
shelf_report([[1, 2], [3, 4]])  ->  {"rows": [3, 7], "columns": [4, 6], "max_row": 1}
```

## Starter

```python
def shelf_report(grid):
    ...
```

## Hints

1. `sum` per row; nested loops or `zip(*grid)` per column; `max` over the row totals with `index`.
2. Column totals: `for c in range(len(grid[0])): total = sum(row[c] for row in grid)` or an inner loop.

## Approach

Three computations sharing the same grid; keep each one simple and assemble the dictionary at the end.

## Reference

```python
def shelf_report(grid):
    rows = []
    for row in grid:
        rows.append(sum(row))
    columns = []
    for c in range(len(grid[0])):
        total = 0
        for row in grid:
            total += row[c]
        columns.append(total)
    return {"rows": rows, "columns": columns, "max_row": rows.index(max(rows))}
```
