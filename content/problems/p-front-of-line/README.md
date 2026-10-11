# Front of the line

Write `next_customer(line)` that returns the name at the front of a
`deque`, without removing it. The line is never empty.

```static
next_customer(deque(["Ada", "Grace"]))  ->  "Ada"
```

## Starter

```python
from collections import deque

def next_customer(line):
    ...
```

## Hints

1. A deque can be indexed like a list.
2. `line[0]`

## Approach

`[0]` peeks at the front; `popleft` would remove it, which the task forbids.

## Reference

```python
from collections import deque

def next_customer(line):
    return line[0]
```
