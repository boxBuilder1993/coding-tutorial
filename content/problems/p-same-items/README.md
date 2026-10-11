# Same items, any order

Two lists hold item names, possibly with repeats and in any order. Write
`same_items(a, b)` that returns `True` if they contain the same set of
distinct items.

```static
same_items(["apple", "milk", "apple"], ["milk", "apple"])  ->  True
same_items(["apple"], ["apple", "milk"])                   ->  False
```

## Starter

```python
def same_items(a, b):
    ...
```

## Hints

1. Sets ignore order and repeats.
2. `set(a) == set(b)`

## Approach

Convert both to sets and compare.

## Reference

```python
def same_items(a, b):
    return set(a) == set(b)
```
