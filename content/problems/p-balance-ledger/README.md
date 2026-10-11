# Running balance

`entries` is a list of `(description, amount)` tuples; positive amounts are
money in, negative money out. Write `ledger(entries)` that returns a list
of strings `<description>: <balance>` showing the balance after each entry,
and stops early with the string `"OVERDRAWN"` as the last line if the balance
ever goes below zero.

```static
ledger([("sale", 50), ("rent", -30), ("sale", 10)])  ->  ["sale: 50", "rent: 20", "sale: 30"]
ledger([("sale", 10), ("rent", -30), ("sale", 100)])  ->  ["sale: 10", "rent: -20", "OVERDRAWN"]
```

## Starter

```python
def ledger(entries):
    ...
```

## Hints

1. Accumulate a balance, format each line, `break` after appending OVERDRAWN.
2. Check `if balance < 0:` after appending the line for that entry.

## Approach

Accumulator with early exit via `break`. The overdrawn line is appended after the entry that caused it.

## Reference

```python
def ledger(entries):
    lines = []
    balance = 0
    for description, amount in entries:
        balance += amount
        lines.append(f"{description}: {balance}")
        if balance < 0:
            lines.append("OVERDRAWN")
            break
    return lines
```
