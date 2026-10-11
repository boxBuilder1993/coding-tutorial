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

1. Check the length, the dash position, and each character's group with `in` and string methods.
2. `code[:3] == code[:3].upper()` with letters, `code[3] == "-"`, and digits in `code[4:]`.

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
