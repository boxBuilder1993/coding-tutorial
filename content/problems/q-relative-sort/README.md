# Sort by another list's order

Write `relative_sort(items, order)` that sorts `items` so values appear in the order
they have in `order`, and any values not in `order` come after, sorted ascending.
`order` has distinct values.

```static
relative_sort([2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6])
    ->  [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]
```

The point is to practise a `key` that looks up a rank in a dictionary.

## Starter

```python
def relative_sort(items, order):
    ...
```

## Hints

1. `rank = {v: i for i, v in enumerate(order)}` gives each ordered value a position.
2. Key: `(0, rank[x])` for values in `order`, `(1, x)` for the rest. Tuples compare first element first.

## Approach

Build a rank dictionary, then sort by a tuple that puts ranked values first in rank order and the rest after in value order. One sort.

## Reference

```python
def relative_sort(items, order):
    rank = {v: i for i, v in enumerate(order)}
    return sorted(items, key=lambda x: (0, rank[x]) if x in rank else (1, x))
```
