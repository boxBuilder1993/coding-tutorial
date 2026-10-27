# Money format

Write `money(amount)` that returns the amount as text with exactly two
decimal places and commas separating thousands.

```static
money(2.5)     ->  "2.50"
money(40)      ->  "40.00"
money(1250)    ->  "1,250.00"
money(1234567.891)  ->  "1,234,567.89"
```

The point is to practise format specs inside an f-string.

## Starter

```python
def money(amount):
    ...
```

## Hints

1. The spec for two decimals is `.2f`; the spec for thousands separators is `,`. They go together after the colon.
2. `f"{amount:,.2f}"`

## Approach

One f-string: `f"{amount:,.2f}"`. The comma comes before the precision.

## Reference

```python
def money(amount):
    return f"{amount:,.2f}"
```
