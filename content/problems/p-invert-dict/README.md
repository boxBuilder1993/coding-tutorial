# Codes to names

`codes` maps item names to product codes, and no two items share a code.
Write `by_code(codes)` that returns the reverse mapping, from code to name.

```static
by_code({"bread": "BRD-001", "milk": "MLK-010"})  ->  {"BRD-001": "bread", "MLK-010": "milk"}
```

## Starter

```python
def by_code(codes):
    ...
```

## Hints

1. Loop over `items()` and assign the other way round.
2. `result[code] = name`

## Approach

Each `(name, code)` pair becomes a `code: name` entry.

## Reference

```python
def by_code(codes):
    result = {}
    for name, code in codes.items():
        result[code] = name
    return result
```
