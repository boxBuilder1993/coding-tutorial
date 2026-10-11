# Longest name

Write `longest(names)` that returns the longest string in the list `names`.
If two are equally long, return the first of them. The list has at least one
name.

```static
longest(["apple", "bread", "sourdough"])  ->  "sourdough"
longest(["milk", "eggs"])                 ->  "milk"
```

## Starter

```python
def longest(names):
    best = names[0]
    for name in names:
        ...
    return best
```

## Hints

1. Compare lengths with `len`, and replace `best` only when the current one is strictly longer.
2. `if len(name) > len(best):` then `best = name`.

## Approach

The "find the biggest" shape: keep the best so far, replace it when something beats it. Strict `>` keeps the first of equals.

## Reference

```python
def longest(names):
    best = names[0]
    for name in names:
        if len(name) > len(best):
            best = name
    return best
```
