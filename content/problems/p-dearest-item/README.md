# Dearest item

`items` is a non-empty list of `(name, price)` tuples. Write
`dearest(items)` that returns the name of the most expensive one.

```static
dearest([("milk", 2.5), ("apple", 40), ("bread", 25)])  ->  "apple"
```

## Starter

```python
def dearest(items):
    ...
```

## Hints

1. `max` with a `key` that picks the price, or a find-the-biggest loop.
2. `max(items, key=lambda p: p[1])[0]`

## Approach

`key=lambda p: p[1]` compares by price; `[0]` of the winning tuple is its name.

## Reference

```python
def dearest(items):
    return max(items, key=lambda p: p[1])[0]
```
