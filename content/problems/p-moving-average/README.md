# Moving average

A sensor sends readings one at a time, and you want the average of the
last `k` readings after each one arrives (or of all readings so far, while
there are fewer than `k`). A `deque` with `maxlen=k` keeps exactly the
last `k`, dropping the oldest by itself.

Write `moving_averages(readings, k)` that returns a list with the average
after each reading, rounded to two decimal places.

```static
moving_averages([10, 20, 30, 40], 2)  ->  [10.0, 15.0, 25.0, 35.0]
moving_averages([3, 6, 9], 5)         ->  [3.0, 4.5, 6.0]
```

## Starter

```python
from collections import deque

def moving_averages(readings, k):
    ...
```

## Hints

1. Append each reading to a `deque(maxlen=k)`, then average what it holds.
2. `round(sum(window) / len(window), 2)` after each append.

## Approach

The bounded deque is the whole technique; `len(window)` handles the warm-up period before it fills.

## Reference

```python
from collections import deque

def moving_averages(readings, k):
    window = deque(maxlen=k)
    result = []
    for r in readings:
        window.append(r)
        result.append(round(sum(window) / len(window), 2))
    return result
```
