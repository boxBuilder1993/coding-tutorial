# First unique character

Write `first_unique(text)` that returns the index of the first character that appears
exactly once in `text`, or `-1` if there is none.

```static
first_unique("leetcode")     ->  0
first_unique("loveleetcode") ->  2
first_unique("aabb")         ->  -1
```

The point is to practise two passes over the same data: count, then scan.

## Starter

```python
def first_unique(text):
    ...
```

## Hints

1. `counts = Counter(text)`.
2. Walk the text again with `enumerate` and return the first index whose character has count 1.

## Approach

A count pass then a scan pass, both linear. The second pass preserves the original order, which a dictionary alone would not.

## Reference

```python
from collections import Counter

def first_unique(text):
    counts = Counter(text)
    for i, ch in enumerate(text):
        if counts[ch] == 1:
            return i
    return -1
```
