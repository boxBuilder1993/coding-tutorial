# Unique items

Write `unique_count(basket)` that returns how many **different** items are
in the list `basket`.

```static
unique_count(["apple", "bread", "apple", "milk", "apple"])  ->  3
unique_count([])                                           ->  0
```

## Starter

```python
def unique_count(basket):
    ...
```

## Hints

1. A set drops duplicates automatically.
2. `len(set(basket))`

## Approach

Convert to a set, take its length.

## Reference

```python
def unique_count(basket):
    return len(set(basket))
```
