# Recent items

Write `last_n(items, n)` that returns a list of the last `n` items of
`items`, in their original order, using a `deque` with `maxlen`. If there
are fewer than `n` items, return all of them.

```static
last_n(["apple", "bread", "milk", "eggs"], 2)  ->  ["milk", "eggs"]
last_n(["apple"], 3)                           ->  ["apple"]
```

## Starter

```python
from collections import deque

def last_n(items, n):
    recent = deque(maxlen=n)
    for item in items:
        ...
    return list(recent)
```

## Hints

1. Append every item; the deque drops the oldest by itself once it is full.
2. `list(recent)` turns the deque into a list for the return.

## Approach

`maxlen` does the work. Slicing with `items[-n:]` is the direct way, but it breaks for `n == 0`, and the deque version works on streams of unknown length.

## Reference

```python
from collections import deque

def last_n(items, n):
    recent = deque(maxlen=n)
    for item in items:
        recent.append(item)
    return list(recent)
```
