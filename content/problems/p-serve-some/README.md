# Serve some customers

`arrivals` is a list of names in arrival order. Write `remaining(arrivals, n)`
that serves the first `n` customers from a queue and returns a list of who
is still waiting. If `n` is more than the number of customers, nobody is left.

```static
remaining(["Ada", "Grace", "Linus"], 2)  ->  ["Linus"]
remaining(["Ada"], 5)                    ->  []
```

## Starter

```python
from collections import deque

def remaining(arrivals, n):
    ...
```

## Hints

1. A deque and a loop that pops from the left `n` times.
2. Stop early if the deque empties: `while n > 0 and line:`.

## Approach

Build a deque, `popleft` up to `n` times while there is anyone left, return what remains as a list.

## Reference

```python
from collections import deque

def remaining(arrivals, n):
    line = deque(arrivals)
    while n > 0 and line:
        line.popleft()
        n -= 1
    return list(line)
```
