# Find a word in a letter grid

`grid` is a list of strings of letters. Write `exists(grid, word)` that returns whether
`word` can be traced through adjacent cells (up, down, left, right), using each cell at
most once.

```static
grid = ["ABCE", "SFCS", "ADEE"]
exists(grid, "ABCCED")  ->  True
exists(grid, "SEE")     ->  True
exists(grid, "ABCB")    ->  False
```

The point is to practise backtracking on a grid with a visited set that is undone.

## Starter

```python
def exists(grid, word):
    ...
```

## Hints

1. Try every cell as a start. `go(r, c, i)`: the cell must be in bounds, unvisited and equal to `word[i]`.
2. If `i` is the last index, success. Mark visited, try the four neighbours with `i + 1`, unmark.
3. Return `True` as soon as any branch succeeds.

## Approach

Depth-first search along the word with a visited set that is removed on backtrack, so cells freed by one failed path are available to another.

## Reference

```python
def exists(grid, word):
    rows, cols = len(grid), len(grid[0])
    visited = set()

    def go(r, c, i):
        if not (0 <= r < rows and 0 <= c < cols) or (r, c) in visited or grid[r][c] != word[i]:
            return False
        if i == len(word) - 1:
            return True
        visited.add((r, c))
        found = any(go(nr, nc, i + 1) for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)))
        visited.remove((r, c))
        return found

    return any(go(r, c, 0) for r in range(rows) for c in range(cols))
```
