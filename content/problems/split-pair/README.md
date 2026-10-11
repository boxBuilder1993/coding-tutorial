# Split a pair

Each stock entry is a tuple `(item, quantity)`. Write `describe(entry)` that
returns the text `<quantity> x <item>`.

```static
describe(("bread", 3))  ->  "3 x bread"
```

## Starter

```python
def describe(entry):
    ...
```

## Hints

1. Unpack the tuple into two names: `item, quantity = entry`.
2. Build the text with an f-string.

## Approach

Unpack, then `return f"{quantity} x {item}"`. Indexing with `entry[0]` and `entry[1]` works but reads worse.

## Reference

```python
def describe(entry):
    item, quantity = entry
    return f"{quantity} x {item}"
```
