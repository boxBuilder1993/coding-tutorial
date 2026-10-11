# Parse a receipt

A receipt is one string with one line per item, each line being
`<item> x <quantity> @ <price>`. Write `receipt_total(text)` that returns
the total cost. Lines may have extra spaces at the ends; blank lines are skipped.

```static
receipt_total("bread x 3 @ 25\nmilk x 2 @ 2.5")  ->  80.0
receipt_total("")                                  ->  0
```

## Starter

```python
def receipt_total(text):
    ...
```

## Hints

1. `split("\n")` for lines, `split()` for the parts of each line, `float` for the numbers.
2. Parts of a line are `[item, "x", qty, "@", price]`; use positions 2 and 4.

## Approach

Split into lines, skip blanks after `strip`, split each line on spaces, convert the quantity and price, accumulate.

## Reference

```python
def receipt_total(text):
    total = 0
    for line in text.split("\n"):
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        total += float(parts[2]) * float(parts[4])
    return total
```
