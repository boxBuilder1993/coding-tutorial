# Validate product codes

A valid product code is three capital letters, a dash, and three digits,
like `BRD-001`. Write `valid_codes(codes)` that returns the list of valid
codes from the input, in order.

```static
valid_codes(["BRD-001", "brd-001", "BRD-01", "MLK-010", "BRD001"])  ->  ["BRD-001", "MLK-010"]
```

## Starter

```python
def valid_codes(codes):
    ...
```

## Hints

1. Check the length and the dash position first, then look at each character of the two parts in turn.
2. Every character of `code[:3]` must be in `"ABCDEFGHIJKLMNOPQRSTUVWXYZ"` and every character of `code[4:]` in `"0123456789"`. A loop with `in` over each part does it.

## Approach

Write a small helper `is_valid(code)` that checks each rule in turn, then filter. Breaking the checks into a helper keeps the loop readable.

## Reference

```python
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGITS = "0123456789"

def is_valid(code):
    if len(code) != 7 or code[3] != "-":
        return False
    for ch in code[:3]:
        if ch not in LETTERS:
            return False
    for ch in code[4:]:
        if ch not in DIGITS:
            return False
    return True

def valid_codes(codes):
    result = []
    for code in codes:
        if is_valid(code):
            result.append(code)
    return result
```
