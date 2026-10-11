# Letter counts

Write `letter_counts(text)` that returns a dictionary mapping each
character in `text` to how many times it appears, ignoring spaces.

```static
letter_counts("a bad cab")  ->  {"a": 3, "b": 2, "d": 1, "c": 1}
```

## Starter

```python
def letter_counts(text):
    ...
```

## Hints

1. The counting pattern with `get`, plus an `if` to skip spaces.
2. `if ch != " ":` then `counts[ch] = counts.get(ch, 0) + 1`.

## Approach

Count with `get(ch, 0) + 1`, skipping the space character.

## Reference

```python
def letter_counts(text):
    counts = {}
    for ch in text:
        if ch != " ":
            counts[ch] = counts.get(ch, 0) + 1
    return counts
```
