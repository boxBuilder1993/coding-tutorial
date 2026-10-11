# Line totals

`lines` is a list of `(item, quantity, price)` tuples. Write
`line_totals(lines)` that returns a list of the total for each line.

```static
line_totals([("bread", 3, 25), ("milk", 2, 2.5)])  ->  [75, 5.0]
```

## Starter

```python
def line_totals(lines):
    ...
```

## Hints

1. A loop that unpacks each tuple.
2. `for item, quantity, price in lines:` then append `quantity * price`.

## Approach

Unpack in the `for` line, multiply, append to a result list.

## Reference

```python
def line_totals(lines):
    totals = []
    for item, quantity, price in lines:
        totals.append(quantity * price)
    return totals
```
