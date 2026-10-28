# Sort by price, then name

`orders` is a list of `(name, price)` tuples. Write `by_price_then_name(orders)`
that returns a new list sorted by price from highest to lowest, with
orders of equal price in alphabetical order of name.

```static
by_price_then_name([("bread", 25), ("apple", 40), ("milk", 25), ("eggs", 60)])
    ->  [("eggs", 60), ("apple", 40), ("bread", 25), ("milk", 25)]
```

The point is to practise a `key` that returns a tuple, with one field
reversed by negation.

## Starter

```python
def by_price_then_name(orders):
    ...
```

## Hints

1. `sorted(orders, key=...)` where the key returns a tuple.
2. The tuple is `(-price, name)`: negative price so bigger prices come first, name as the tie-breaker ascending.

## Approach

One call: `sorted(orders, key=lambda o: (-o[1], o[0]))`. `reverse=True` would reverse the names as well, which is why negation is used instead.

## Reference

```python
def by_price_then_name(orders):
    return sorted(orders, key=lambda o: (-o[1], o[0]))
```
