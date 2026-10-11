# Comma list

Write `listing(items)` that returns the items joined into one string
separated by a comma and a space.

```static
listing(["apple", "bread", "milk"])  ->  "apple, bread, milk"
listing([])                          ->  ""
```

## Starter

```python
def listing(items):
    ...
```

## Hints

1. `join`, called on the separator.
2. `", ".join(items)`

## Approach

`join` is a method of the separator string and takes the list.

## Reference

```python
def listing(items):
    return ", ".join(items)
```
