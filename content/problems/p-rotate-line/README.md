# Rotate the line

Write `rotate(line, k)` that moves the front person of a `deque` to the back,
`k` times over, and returns the same deque, changed in place. `k` may be
larger than the line, or zero.

```static
rotate(deque(["a", "b", "c"]), 1)  ->  deque(["b", "c", "a"])
rotate(deque(["a", "b", "c"]), 3)  ->  deque(["a", "b", "c"])
rotate(deque(["a", "b", "c"]), 4)  ->  deque(["b", "c", "a"])
```

## Starter

```python
from collections import deque

def rotate(line, k):
    ...
```

## Hints

1. Moving one person from the front to the back is two deque operations. Repeat them `k` times.
2. `for _ in range(k): line.append(line.popleft())`, with a check for an empty deque first, since `popleft` on an empty one is an error.

## Approach

`k` single moves in a loop. The empty-deque guard is the part most people forget.

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
