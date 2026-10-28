# Longest common subsequence

Write `lcs(a, b)` that returns the length of the longest sequence of characters that
appears in both strings in the same order, not necessarily adjacent.

```static
lcs("abcde", "ace")  ->  3
lcs("abc", "def")    ->  0
lcs("", "abc")       ->  0
```

The point is to practise a two-string DP table: `table[i][j]` for the first `i` characters
of `a` and the first `j` of `b`.

## Starter

```python
def lcs(a, b):
    ...
```

## Hints

1. If `a[i - 1] == b[j - 1]`, `table[i][j] = table[i - 1][j - 1] + 1`.
2. Otherwise `max(table[i - 1][j], table[i][j - 1])`. Row and column 0 are zeros.

## Approach

Matching characters extend the best answer for the two shorter prefixes; otherwise drop a character from one side or the other. `len(a) * len(b)` cells.

## Reference

```python
def lcs(a, b):
    table = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])
    return table[len(a)][len(b)]
```
