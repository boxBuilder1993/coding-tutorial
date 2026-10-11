# What is in stock

`stock` maps items to quantities. Write `available(stock)` that returns the
names of items with quantity above zero, alphabetically.

```static
available({"milk": 0, "apple": 3, "bread": 1})  ->  ["apple", "bread"]
```

## Starter

```python
def available(stock):
    ...
```

## Hints

1. Loop over `items()`, keep names where the quantity is positive, sort.
2. `if qty > 0: names.append(item)` then `sorted(names)`.

## Approach

Filter then sort.

## Reference

```python
def available(stock):
    names = []
    for item, qty in stock.items():
        if qty > 0:
            names.append(item)
    return sorted(names)
```
