# Has the prefix?

Every bakery product code starts with `BRD-`. Write `is_bakery(code)` that
returns `True` if `code` starts with that prefix and `False` otherwise.

```static
is_bakery("BRD-001")  ->  True
is_bakery("MLK-010")  ->  False
```

## Starter

```python
def is_bakery(code):
    ...
```

## Hints

1. Strings have a `startswith` method that returns a boolean.
2. `return code.startswith("BRD-")`

## Approach

`startswith` does exactly this. Slicing, `code[:4] == "BRD-"`, is the manual version.

## Reference

```python
def is_bakery(code):
    return code.startswith("BRD-")
```
