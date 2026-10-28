# Count the islands

`grid` is a list of strings of equal length made of `"1"` (land) and
`"0"` (water). An island is a group of land cells connected up, down,
left or right (not diagonally). Write `count_islands(grid)` that returns
how many islands there are.

```static
count_islands([
    "11000",
    "11000",
    "00100",
    "00011",
])  ->  3
count_islands(["000"])  ->  0
```

The point is to practise treating a grid as a graph: neighbours are
computed from coordinates and checked against the bounds.

## Starter

```python
def count_islands(grid):
    ...
```

## Hints

1. Loop over every cell. When you find land not yet seen, count one island and flood from it.
2. Flood with a stack of `(row, col)` tuples and a `seen` set; for each cell push its four in-bounds land neighbours.
3. `0 <= r < rows and 0 <= c < cols` is the bounds check; do it before indexing.

## Approach

Connected components on an implicit graph. The outer double loop finds the start of each island; the flood marks every cell of it so it is not counted again.

## Reference

```python
def count_islands(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    seen = set()
    islands = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "1" or (r, c) in seen:
                continue
            islands += 1
            stack = [(r, c)]
            while stack:
                cr, cc = stack.pop()
                if (cr, cc) in seen:
                    continue
                seen.add((cr, cc))
                for nr, nc in ((cr - 1, cc), (cr + 1, cc), (cr, cc - 1), (cr, cc + 1)):
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                        stack.append((nr, nc))
    return islands
```
