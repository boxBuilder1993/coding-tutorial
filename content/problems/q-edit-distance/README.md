# Edit distance

Write `edit_distance(a, b)` that returns the fewest single-character insertions, deletions
or replacements needed to turn `a` into `b`.

```static
edit_distance("horse", "ros")          ->  3
edit_distance("intention", "execution")  ->  5
edit_distance("", "abc")               ->  3
```

The point is to practise a two-string table with three choices per cell.

## Starter

```python
def edit_distance(a, b):
    ...
```

## Hints

1. `table[i][0] = i` and `table[0][j] = j`: turning a prefix into nothing or nothing into a prefix.
2. If the characters match, `table[i][j] = table[i - 1][j - 1]`; else `1 + min(delete, insert, replace)` = `1 + min(table[i - 1][j], table[i][j - 1], table[i - 1][j - 1])`.

## Approach

Each cell asks: how did the last characters line up? Equal, or fixed by one of the three edits. `len(a) * len(b)` cells.

## Reference

```python
def edit_distance(a, b):
    table = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(len(a) + 1):
        table[i][0] = i
    for j in range(len(b) + 1):
        table[0][j] = j
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                table[i][j] = table[i - 1][j - 1]
            else:
                table[i][j] = 1 + min(table[i - 1][j], table[i][j - 1], table[i - 1][j - 1])
    return table[len(a)][len(b)]
```
