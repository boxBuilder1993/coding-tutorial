# Middle item

Write `middle(items)` that returns the item in the middle of a list with an
odd number of items.

```static
middle(["apple", "bread", "milk"])  ->  "bread"
middle([7])                         ->  7
```

## Starter

```python
def middle(items):
    ...
```

## Hints

1. Indexing with a computed position.
2. The middle position is `len(items) // 2`.

## Approach

Integer division gives the middle index for odd lengths: 3 // 2 is 1.

## Reference

```python
def middle(items):
    return items[len(items) // 2]
```
