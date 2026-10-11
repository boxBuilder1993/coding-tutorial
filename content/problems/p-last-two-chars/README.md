# Last two characters

Write `suffix(code)` that returns the last two characters of a string that
has at least two characters.

```static
suffix("BRD-001")  ->  "01"
```

## Starter

```python
def suffix(code):
    ...
```

## Hints

1. A slice with a negative start.
2. `code[-2:]`

## Approach

Negative slice from two before the end.

## Reference

```python
def suffix(code):
    return code[-2:]
```
