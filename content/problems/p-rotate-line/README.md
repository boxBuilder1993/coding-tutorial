# Rotate the line

Write `rotate(line, k)` that moves the front person of a `deque` to the back
`k` times and returns the deque. `k` may be larger than the line.

```static
rotate(deque(["a", "b", "c"]), 1)  ->  deque(["b", "c", "a"])
rotate(deque(["a", "b", "c"]), 4)  ->  deque(["b", "c", "a"])
```

## Starter

```python
from collections import deque

def rotate(line, k):
    ...
```

## Hints

1. A `for` over `range(k)` doing `popleft` then `append`.
2. Guard for an empty deque, or use `line.rotate(-k)` which handles everything.

## Approach

`k` single rotations in a loop. `deque.rotate(-k)` is the built-in equivalent.

## Reference

```python
from collections import deque

def rotate(line, k):
    if not line:
        return line
    for _ in range(k):
        line.append(line.popleft())
    return line
```
