# In both shops

Two shops each have a list of items. Write `in_both(a, b)` that returns a
list of the items that appear in both, each item once, in any order.

```static
in_both(["apple", "bread", "milk"], ["milk", "eggs", "apple"])  ->  ["apple", "milk"]   (or ["milk", "apple"])
in_both(["apple"], ["bread"])                                   ->  []
```

## Starter

```python
def in_both(a, b):
    ...
```

## Hints

1. Turn both lists into sets and use `&` for what they share.
2. `list(...)` turns the resulting set back into a list.

## Approach

`return list(set(a) & set(b))`. A loop with `if item in b and item not in result` works too but is slower for big lists.

## Reference

```python
def in_both(a, b):
    return list(set(a) & set(b))
```
