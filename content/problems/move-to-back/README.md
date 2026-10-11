# Move to the back

A customer at the front of the line forgot their wallet and goes to the back.
Write `to_back(line)` that takes a `deque`, moves the front item to the back,
and returns the same deque. An empty deque is returned unchanged.

```static
to_back(deque(["Ada", "Grace", "Linus"]))  ->  deque(["Grace", "Linus", "Ada"])
```

## Starter

```python
from collections import deque

def to_back(line):
    ...
```

## Hints

1. `popleft()` to take the front, `append()` to put it at the back.
2. Guard with `if line:` so an empty deque does not raise.

## Approach

Two operations. `deque` also has `rotate(-1)`, which does exactly this in one call.

## Reference

```python
from collections import deque

def to_back(line):
    if line:
        line.append(line.popleft())
    return line
```
