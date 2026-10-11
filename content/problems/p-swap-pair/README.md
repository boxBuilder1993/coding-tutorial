# Swap a pair

Write `swap(pair)` that takes a tuple of two values and returns a tuple
with them the other way round.

```static
swap(("bread", 25))  ->  (25, "bread")
```

## Starter

```python
def swap(pair):
    ...
```

## Hints

1. Unpack, then build a new tuple.
2. `a, b = pair` then `return (b, a)`

## Approach

Unpacking into two names makes the swap obvious. `return pair[1], pair[0]` also works.

## Reference

```python
def swap(pair):
    a, b = pair
    return (b, a)
```
