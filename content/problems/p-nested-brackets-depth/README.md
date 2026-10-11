# Deepest nesting

Write `max_depth(text)` that returns how deeply the round brackets in
`text` nest. Unbalanced text returns `-1`. Other characters are ignored.

```static
max_depth("(a(b)(c(d)))")  ->  3
max_depth("()")            ->  1
max_depth("")              ->  0
max_depth("(()")           ->  -1
```

## Starter

```python
def max_depth(text):
    ...
```

## Hints

1. A counter instead of a stack: `+1` on `(`, `-1` on `)`, track the maximum.
2. If the counter ever goes negative, or is not zero at the end, return -1.

## Approach

The stack from the brackets problems only ever holds `(`, so its size is all that matters; a counter replaces it.

## Reference

```python
def max_depth(text):
    depth = 0
    best = 0
    for ch in text:
        if ch == "(":
            depth += 1
            best = max(best, depth)
        elif ch == ")":
            depth -= 1
            if depth < 0:
                return -1
    if depth != 0:
        return -1
    return best
```
