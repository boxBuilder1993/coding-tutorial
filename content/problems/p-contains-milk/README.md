# Contains milk?

Write `has_milk(order)` that returns `True` if the word `milk` appears
anywhere in the order text, in any mix of capitals.

```static
has_milk("2 x Milk, 1 x bread")  ->  True
has_milk("bread")                ->  False
```

## Starter

```python
def has_milk(order):
    ...
```

## Hints

1. Lowercase the text, then `in`.
2. `"milk" in order.lower()`

## Approach

Normalise case first so `Milk` and `MILK` both match.

## Reference

```python
def has_milk(order):
    return "milk" in order.lower()
```
