# Solve a Sudoku

`grid` is a list of nine strings of nine characters, digits `1`-`9` or `.` for empty, with
exactly one solution. Write `solve(grid)` that returns the solved grid in the same format.

```static
solve(["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"])
    ->  ["534678912", "672195348", "198342567", "859761423", "426853791", "713924856", "961537284", "287419635", "345286179"]
```

Backtracking cell by cell: for an empty cell, try each digit not already in its row,
column or 3x3 box; recurse; undo. Keep three lists of sets so the legality check is
constant time.

## Starter

```python
def solve(grid):
    ...
```

## Hints

1. Convert to a list of lists. Build `rows[r]`, `cols[c]`, `boxes[(r // 3) * 3 + c // 3]` as sets of used digits, and a list of empty cells.
2. `go(k)`: if `k == len(empties)` return `True`. For digit in `'123456789'` not in the three sets: place it in the grid and sets, recurse, remove on failure.
3. Return `[''.join(row) for row in cells]`.

## Approach

Depth-first search over empty cells with constant-time constraint checks. Choosing the cell with the fewest candidates first speeds it up but is not needed for a one-solution puzzle.

## Reference

```python
def solve(grid):
    cells = [list(row) for row in grid]
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    empties = []
    for r in range(9):
        for c in range(9):
            ch = cells[r][c]
            if ch == ".":
                empties.append((r, c))
            else:
                rows[r].add(ch)
                cols[c].add(ch)
                boxes[(r // 3) * 3 + c // 3].add(ch)

    def go(k):
        if k == len(empties):
            return True
        r, c = empties[k]
        b = (r // 3) * 3 + c // 3
        for d in "123456789":
            if d in rows[r] or d in cols[c] or d in boxes[b]:
                continue
            cells[r][c] = d
            rows[r].add(d); cols[c].add(d); boxes[b].add(d)
            if go(k + 1):
                return True
            rows[r].remove(d); cols[c].remove(d); boxes[b].remove(d)
            cells[r][c] = "."
        return False

    go(0)
    return ["".join(row) for row in cells]
```
