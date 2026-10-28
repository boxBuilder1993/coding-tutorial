# Longest increasing path in a grid

`grid` is a list of lists of whole numbers. Write `longest_path(grid)` that returns the
number of cells in the longest path that moves up, down, left or right and strictly
increases at every step.

```static
longest_path([[9, 9, 4], [6, 6, 8], [2, 1, 1]])  ->  4     (1, 2, 6, 9)
longest_path([[3, 4, 5], [3, 2, 6], [2, 2, 1]])  ->  4
longest_path([[1]])                              ->  1
```

Depth-first search from each cell with memoisation of "longest path starting here". No
visited set is needed: strictly increasing means no cycles.

## Starter

```python
def longest_path(grid):
    ...
```

## Hints

1. `memo[(r, c)]` = longest increasing path starting at that cell.
2. `go(r, c) = 1 + max(go(nr, nc) for in-bounds neighbours with a larger value, default 0)`.
3. Answer is the max over all cells.

## Approach

Memoised DFS on an implicit DAG. Each cell is computed once; linear in cells.

## Reference

```python
def longest_path(grid):
    rows, cols = len(grid), len(grid[0])
    memo = {}

    def go(r, c):
        if (r, c) in memo:
            return memo[(r, c)]
        best = 1
        for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] > grid[r][c]:
                best = max(best, 1 + go(nr, nc))
        memo[(r, c)] = best
        return best

    return max(go(r, c) for r in range(rows) for c in range(cols))
```
