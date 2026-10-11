# Boxes and crates

Write `labels(n)` that returns a list of strings for the numbers 1 to `n`:
`"Box"` if the number is divisible by 3, `"Crate"` if divisible by 5,
`"BoxCrate"` if divisible by both, otherwise the number as text.

```static
labels(6)  ->  ["1", "2", "Box", "4", "Crate", "Box"]
```

## Starter

```python
def labels(n):
    ...
```

## Hints

1. `range(1, n + 1)`, `%`, and an `if` chain with the "both" case first.
2. Check `% 15 == 0` before `% 3` and `% 5`, and use `str(i)` for the default.

## Approach

The order of the `if` chain matters: test the combined case first or it is never reached.

## Reference

```python
def labels(n):
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("BoxCrate")
        elif i % 3 == 0:
            result.append("Box")
        elif i % 5 == 0:
            result.append("Crate")
        else:
            result.append(str(i))
    return result
```
