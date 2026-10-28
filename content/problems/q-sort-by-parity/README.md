# Evens first

Write `evens_first(items)` that returns the list with all even numbers before all odd
numbers, keeping the original relative order within the evens and within the odds.

```static
evens_first([3, 1, 2, 4, 5, 6])  ->  [2, 4, 6, 3, 1, 5]
evens_first([1, 3])              ->  [1, 3]
```

The point is to practise stable sorting by a boolean key.

## Starter

```python
def evens_first(items):
    ...
```

## Hints

1. `sorted(items, key=lambda x: x % 2)` works because `sorted` is stable: equal keys keep their order.
2. Two list comprehensions, evens then odds, also work.

## Approach

A key of `x % 2` is 0 for evens and 1 for odds. Because `sorted` is stable, items with the same key stay in input order.

## Reference

```python
def evens_first(items):
    return sorted(items, key=lambda x: x % 2)
```
