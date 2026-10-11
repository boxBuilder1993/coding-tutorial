# Expand shelf ranges

Shelf labels are given as a string like `"3-5, 8, 10-11"`: comma-separated,
each part either a single number or a range `a-b` inclusive. Write
`expand(text)` that returns the full list of numbers in order.

```static
expand("3-5, 8, 10-11")  ->  [3, 4, 5, 8, 10, 11]
expand("7")              ->  [7]
```

## Starter

```python
def expand(text):
    ...
```

## Hints

1. `split(",")`, `strip`, then check for `"-"` in each part.
2. For a range, `a, b = part.split("-")` and `range(int(a), int(b) + 1)`.

## Approach

Two levels of splitting with a branch for ranges. Remember `range` excludes the stop, so add one.

## Reference

```python
def expand(text):
    result = []
    for part in text.split(","):
        part = part.strip()
        if "-" in part:
            a, b = part.split("-")
            for n in range(int(a), int(b) + 1):
                result.append(n)
        else:
            result.append(int(part))
    return result
```
