# Numbered receipt

Write `numbered(items)` that returns a list of strings, one per item,
numbered from 1: `"1. apple"`, `"2. bread"`, and so on.

```static
numbered(["apple", "bread"])  ->  ["1. apple", "2. bread"]
numbered([])                  ->  []
```

## Starter

```python
def numbered(items):
    lines = []
    for ... in enumerate(items, start=1):
        ...
    return lines
```

## Hints

1. `enumerate(items, start=1)` gives `(number, item)` pairs; unpack them in the `for`.
2. `lines.append(f"{i}. {item}")`

## Approach

`enumerate` with `start=1` avoids adding one by hand. Build each line with an f-string and append.

## Reference

```python
def numbered(items):
    lines = []
    for i, item in enumerate(items, start=1):
        lines.append(f"{i}. {item}")
    return lines
```
