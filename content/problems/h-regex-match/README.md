# Pattern matching with . and *

Write `matches(text, pattern)` that returns whether the whole of `text` matches `pattern`,
where `.` matches any single character and `*` means "zero or more of the preceding
element". Patterns are valid: `*` never comes first.

```static
matches("aa", "a")     ->  False
matches("aa", "a*")    ->  True
matches("ab", ".*")    ->  True
matches("aab", "c*a*b")  ->  True
matches("mississippi", "mis*is*p*.")  ->  False
```

A two-index DP: `ok[i][j]` means `text[i:]` matches `pattern[j:]`. The `*` case branches
into "skip the pair" or "consume one character and stay".

## Starter

```python
def matches(text, pattern):
    ...
```

## Hints

1. `ok[len(text)][len(pattern)] = True`. Fill `i` from `len(text)` down and `j` from `len(pattern) - 1` down.
2. `first = i < len(text) and pattern[j] in (text[i], '.')`.
3. If `j + 1 < len(pattern)` and `pattern[j + 1] == '*'`: `ok[i][j] = ok[i][j + 2] or (first and ok[i + 1][j])`. Else `ok[i][j] = first and ok[i + 1][j + 1]`.

## Approach

Each cell asks whether the remaining text matches the remaining pattern, with the star deciding between zero repetitions and one more. Text length times pattern length.

## Reference

```python
def matches(text, pattern):
    n, m = len(text), len(pattern)
    ok = [[False] * (m + 1) for _ in range(n + 1)]
    ok[n][m] = True
    for i in range(n, -1, -1):
        for j in range(m - 1, -1, -1):
            first = i < n and pattern[j] in (text[i], ".")
            if j + 1 < m and pattern[j + 1] == "*":
                ok[i][j] = ok[i][j + 2] or (first and ok[i + 1][j])
            else:
                ok[i][j] = first and ok[i + 1][j + 1]
    return ok[0][0]
```
