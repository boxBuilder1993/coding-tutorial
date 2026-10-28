# Is the string an interleaving?

Write `is_interleaving(a, b, c)` that returns whether `c` can be formed by merging `a` and
`b` while keeping the characters of each in their original order.

```static
is_interleaving("aabcc", "dbbca", "aadbbcbcac")  ->  True
is_interleaving("aabcc", "dbbca", "aadbbbaccc")  ->  False
is_interleaving("", "", "")                      ->  True
```

A table `ok[i][j]`: can the first `i` of `a` and first `j` of `b` make the first `i + j` of
`c`? A cell is true if the previous character of `c` came from `a` or from `b`.

## Starter

```python
def is_interleaving(a, b, c):
    ...
```

## Hints

1. Length check first: `len(a) + len(b) == len(c)`.
2. `ok[0][0] = True`. `ok[i][j] = (i > 0 and ok[i - 1][j] and a[i - 1] == c[i + j - 1]) or (j > 0 and ok[i][j - 1] and b[j - 1] == c[i + j - 1])`.

## Approach

Two-pointer greedy fails when both strings offer the same next character; the table tries both. `len(a) * len(b)` cells.

## Reference

```python
def is_interleaving(a, b, c):
    if len(a) + len(b) != len(c):
        return False
    ok = [[False] * (len(b) + 1) for _ in range(len(a) + 1)]
    ok[0][0] = True
    for i in range(len(a) + 1):
        for j in range(len(b) + 1):
            if i > 0 and ok[i - 1][j] and a[i - 1] == c[i + j - 1]:
                ok[i][j] = True
            if j > 0 and ok[i][j - 1] and b[j - 1] == c[i + j - 1]:
                ok[i][j] = True
    return ok[len(a)][len(b)]
```
