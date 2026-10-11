# Transpose a table

A table is a list of rows, each a list of the same length. Write
`transpose(table)` that returns the table with rows and columns swapped.

```static
transpose([[1, 2, 3], [4, 5, 6]])  ->  [[1, 4], [2, 5], [3, 6]]
transpose([])                      ->  []
```

## Starter

```python
def transpose(table):
    ...
```

## Hints

1. Loop over column positions and collect that position from every row.
2. `for c in range(len(table[0])): column = [row[c] for row in table]`, or an inner `for` loop.

## Approach

Nested loops with the column index outside. Guard the empty table because `table[0]` would fail.

## Reference

```python
def transpose(table):
    if not table:
        return []
    result = []
    for c in range(len(table[0])):
        column = []
        for row in table:
            column.append(row[c])
        result.append(column)
    return result
```
