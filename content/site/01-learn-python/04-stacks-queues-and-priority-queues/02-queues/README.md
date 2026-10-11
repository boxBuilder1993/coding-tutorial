# Queues

A **queue** is a line at the counter. People join at the back and are served
from the front, so the first in is the first out. Anything that must be
handled in arrival order is a queue: customers, print jobs, messages.

## Why not a list?

A list can do it: `append` at the back, `pop(0)` at the front. But `pop(0)`
has to shift every remaining item one place left, so it gets slower as the
list grows. For a few items nobody notices. For thousands it matters.

Python's standard library has a type built for this: `deque` (say "deck"),
from the `collections` module. It is fast at **both** ends.

```python
from collections import deque

line = deque()
line.append("Ada")
line.append("Grace")
line.append("Linus")
print(line)

served = line.popleft()
print("Serving", served)
print(line)
```

`append` adds at the back as usual. `popleft` removes and returns the item at
the front. The `from collections import deque` line brings the type in;
`collections` is part of Python, nothing to install.

## The rest of deque

A `deque` works like a list for most things: `len`, `in`, looping, `[0]` for
the front and `[-1]` for the back. It also has `appendleft` and `pop`, so it
can be a stack too, or a line that people can jump.

```python
from collections import deque

line = deque(["Ada", "Grace"])
line.appendleft("Linus")
print(line)
print(line[0], line[-1])
print(len(line))
```

## Only the last few

`deque(maxlen=n)` keeps at most `n` items. Adding to a full one silently
drops the item at the other end. That is exactly "the last three things that
happened".

```python
from collections import deque

recent = deque(maxlen=3)
for item in ["apple", "bread", "milk", "eggs", "flour"]:
    recent.append(item)
    print(list(recent))
```

## The queue loop

The standard shape: while the queue is not empty, take from the front, deal
with it, and possibly add new things to the back. It is how you process work
that generates more work, and it comes back in the algorithms track as
breadth-first search.

```python
from collections import deque

orders = deque(["bread", "cake"])
while orders:
    order = orders.popleft()
    print("Making", order)
    if order == "cake":
        orders.append("icing")
```

## Try it

:::problem serve-in-order

:::problem move-to-back

:::problem recent-items

Next: [Priority queues](../03-priority-queues).
