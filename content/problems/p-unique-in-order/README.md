# Unique, in order

Write `unique(items)` that returns a new list with duplicates removed,
keeping the first occurrence of each item and the original order.

```static
unique(["apple", "bread", "apple", "milk", "bread"])  ->  ["apple", "bread", "milk"]
```

## Starter

```python
def unique(items):
    ...
```

## Hints

1. A set to remember what you have seen, a list for the result.
2. `if item not in seen:` add to both.

## Approach

`set(items)` alone loses the order. Walk the list, skip anything already in the seen-set.

## Reference

```python
def unique(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
```
