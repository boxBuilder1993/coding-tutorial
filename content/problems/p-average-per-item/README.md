# Average per item

`history` maps each item to a non-empty list of prices it has been sold at.
Write `averages(history)` that returns a dictionary of each item's average
price, rounded to two decimal places.

```static
averages({"apple": [40, 42], "milk": [2.5]})  ->  {"apple": 41.0, "milk": 2.5}
```

## Starter

```python
def averages(history):
    ...
```

## Hints

1. Loop over `items()`; `sum` and `len` for the average; `round`.
2. `result[item] = round(sum(prices) / len(prices), 2)`

## Approach

One dictionary in, one out, with the average computed per entry.

## Reference

```python
def averages(history):
    result = {}
    for item, prices in history.items():
        result[item] = round(sum(prices) / len(prices), 2)
    return result
```
