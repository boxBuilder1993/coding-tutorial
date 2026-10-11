# In both shops

Two shops each have a list of items. Write `in_both(a, b)` that returns a
**sorted list** of the items that appear in both.

```static
in_both(["apple", "bread", "milk"], ["milk", "eggs", "apple"])  ->  ["apple", "milk"]
in_both(["apple"], ["bread"])                                   ->  []
```

## Starter

```python
def in_both(a, b):
    ...
```

## Hints

1. Turn both lists into sets and use `&` for what they share.
2. `sorted(...)` turns the resulting set into a sorted list.

## Approach

`return sorted(set(a) & set(b))`. A loop with `if item in b` works too but is slower for big lists.

## Reference

```python
def in_both(a, b):
    return sorted(set(a) & set(b))
```
