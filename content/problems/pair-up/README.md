# Pair up items and prices

Write `price_table(items, prices)` that returns a dictionary mapping each
item to the price at the same position. The two lists are the same length.

```static
price_table(["apple", "bread"], [40, 25])  ->  {"apple": 40, "bread": 25}
```

## Starter

```python
def price_table(items, prices):
    ...
```

## Hints

1. `zip(items, prices)` pairs them up position by position.
2. `dict(...)` turns a sequence of pairs into a dictionary.

## Approach

`return dict(zip(items, prices))`. A `for item, price in zip(...)` loop that assigns into an empty dict is the longer form.

## Reference

```python
def price_table(items, prices):
    return dict(zip(items, prices))
```
