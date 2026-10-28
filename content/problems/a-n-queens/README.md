# N-queens

Write `n_queens(n)` that returns how many ways `n` queens can be placed on
an `n × n` board so that no two share a row, column or diagonal.

```static
n_queens(1)  ->  1
n_queens(4)  ->  2
n_queens(8)  ->  92
```

The point is to practise backtracking with pruning: one queen per row,
and three sets that make "is this square attacked" a constant-time check.
`n_queens(9)` is checked, so unpruned search will not do.

## Starter

```python
def n_queens(n):
    ...
```

## Hints

1. Recurse over rows; in each row try every column.
2. Keep sets `cols`, `diag1` (`row - col`) and `diag2` (`row + col`). Skip a column if any set already has its value.
3. Add to all three sets before recursing and remove after. Count when `row == n`.

## Approach

Placing by rows means rows never clash. Columns and the two diagonal families are tracked in sets so each candidate square is checked in constant time and rejected before any deeper work. Undo the three additions after each recursive call.

## Reference

```python
def n_queens(n):
    count = 0
    cols, diag1, diag2 = set(), set(), set()

    def go(row):
        nonlocal count
        if row == n:
            count += 1
            return
        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            go(row + 1)
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

    go(0)
    return count
```
