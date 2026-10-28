# Sort by frequency

Write `by_frequency(items)` that returns the list sorted so the most frequent values
come first. Values with the same frequency are ordered smallest first, and all copies
of a value stay together.

```static
by_frequency([4, 1, 2, 2, 3, 3, 3])  ->  [3, 3, 3, 2, 2, 1, 4]
by_frequency([])                     ->  []
```

The point is to practise a `key` built from a `Counter`.

## Starter

```python
def by_frequency(items):
    ...
```

## Hints

1. Count first: `counts = Counter(items)`.
2. Sort with `key=lambda x: (-counts[x], x)`.

## Approach

One count, one sort with a two-part key. Negating the count puts frequent values first while leaving the value tie-break ascending.

## Reference

```python
from collections import Counter

def by_frequency(items):
    counts = Counter(items)
    return sorted(items, key=lambda x: (-counts[x], x))
```
