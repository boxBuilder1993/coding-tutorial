# Copy, then extend

Write `with_extra(items, extra)` that returns a new list containing
everything in `items` followed by `extra`, **without changing** `items`.

```static
with_extra(["apple", "bread"], "milk")  ->  ["apple", "bread", "milk"]
```

## Starter

```python
def with_extra(items, extra):
    ...
```

## Hints

1. `copy = items` does not copy; both names share one list.
2. `items[:]` makes a real copy. Append to that and return it.

## Approach

Slice to copy, append, return. `items + [extra]` builds the new list in one expression and is also fine.

## Reference

```python
def with_extra(items, extra):
    copy = items[:]
    copy.append(extra)
    return copy
```
