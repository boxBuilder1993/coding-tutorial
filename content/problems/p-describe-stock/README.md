# Describe stock

Write `describe(item, quantity)` that returns the text `<item>: <quantity> left`.

```static
describe("bread", 3)  ->  "bread: 3 left"
```

## Starter

```python
def describe(item, quantity):
    ...
```

## Hints

1. An f-string.
2. `f"{item}: {quantity} left"`

## Approach

One f-string with both values.

## Reference

```python
def describe(item, quantity):
    return f"{item}: {quantity} left"
```
