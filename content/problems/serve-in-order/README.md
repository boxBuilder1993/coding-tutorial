# Serve in order

`arrivals` is a list of customer names in the order they joined the line.
Write `serve_all(arrivals)` that uses a `deque` to serve them one at a time
from the front, and returns a list of the names in the order they were served.

```static
serve_all(["Ada", "Grace", "Linus"])  ->  ["Ada", "Grace", "Linus"]
```

It looks trivial, and it is: the point is to write the queue loop once.

## Starter

```python
from collections import deque

def serve_all(arrivals):
    line = deque(arrivals)
    served = []
    while line:
        ...
    return served
```

## Hints

1. `line.popleft()` takes the person at the front.
2. Append each served person to `served`.

## Approach

The queue loop: while not empty, take from the front, record it.

## Reference

```python
from collections import deque

def serve_all(arrivals):
    line = deque(arrivals)
    served = []
    while line:
        served.append(line.popleft())
    return served
```
