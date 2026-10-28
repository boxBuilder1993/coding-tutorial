# Common items with counts

Write `intersection(a, b)` that returns the values that appear in both lists, with each
value appearing as many times as it appears in both (the smaller of its two counts),
sorted ascending.

```static
intersection([1, 2, 2, 1], [2, 2])      ->  [2, 2]
intersection([4, 9, 5], [9, 4, 9, 8, 4]) ->  [4, 9]
```

The point is to practise Counter intersection.

## Starter

```python
def intersection(a, b):
    ...
```

## Hints

1. `Counter(a) & Counter(b)` keeps each value with the smaller of the two counts.
2. `.elements()` expands a Counter back into repeated values; sort the result.

## Approach

One Counter intersection then expand and sort. The `&` operator is the whole algorithm.

## Reference

```python
from collections import Counter

def intersection(a, b):
    return sorted((Counter(a) & Counter(b)).elements())
```
