# Longest palindromic subsequence

Write `lps(text)` that returns the length of the longest subsequence of `text` (characters
in order, not necessarily adjacent) that is a palindrome.

```static
lps("bbbab")  ->  4     (bbbb)
lps("cbbd")   ->  2
lps("")       ->  0
```

A table over substrings `text[i..j]`: equal ends add 2 to the inside, otherwise take the
better of dropping one end. Fill by increasing length. Equivalent to the longest common
subsequence of the text with its reverse.

## Starter

```python
def lps(text):
    ...
```

## Hints

1. `table[i][j]` for `i <= j`; single characters are 1.
2. If `text[i] == text[j]`, `table[i][j] = table[i + 1][j - 1] + 2` (or 2 when `j == i + 1`); else `max(table[i + 1][j], table[i][j - 1])`.
3. Fill `i` from `n - 1` down to 0 and `j` from `i + 1` up, so the needed entries exist.

## Approach

Interval DP: the answer for a span depends on spans inside it. Quadratic in the length.

## Reference

```python
def lps(text):
    n = len(text)
    if n == 0:
        return 0
    table = [[0] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
        table[i][i] = 1
        for j in range(i + 1, n):
            if text[i] == text[j]:
                table[i][j] = (table[i + 1][j - 1] if j > i + 1 else 0) + 2
            else:
                table[i][j] = max(table[i + 1][j], table[i][j - 1])
    return table[0][n - 1]
```
