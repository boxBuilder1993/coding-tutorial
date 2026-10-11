# Group by first letter

Write `by_letter(items)` that returns a dictionary mapping each first
letter to the list of items starting with it, in their original order.

```static
by_letter(["apple", "bread", "apricot"])  ->  {"a": ["apple", "apricot"], "b": ["bread"]}
```

## Starter

```python
def by_letter(items):
    ...
```

## Hints

1. A dictionary of lists; create the list the first time a letter is seen.
2. `if letter not in groups: groups[letter] = []` then `groups[letter].append(item)`.

## Approach

The grouping pattern: check for the key, create an empty list if new, append.

## Reference

```python
def by_letter(items):
    groups = {}
    for item in items:
        letter = item[0]
        if letter not in groups:
            groups[letter] = []
        groups[letter].append(item)
    return groups
```
