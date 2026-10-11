# A queue with VIPs

Customers arrive as `(name, is_vip)` tuples. VIPs go to the front of the
line, behind any VIPs already there; everyone else joins the back. Write
`serving_order(arrivals)` that returns the order in which everyone is served.

```static
serving_order([("Ada", False), ("Grace", True), ("Linus", False), ("Ken", True)])  ->  ["Grace", "Ken", "Ada", "Linus"]
```

## Starter

```python
from collections import deque

def serving_order(arrivals):
    ...
```

## Hints

1. Two deques, one for VIPs and one for everyone else, each in arrival order.
2. Serve the whole VIP deque first, then the other; or a single deque with `appendleft` and a VIP count.

## Approach

Keep two queues, since VIPs are a queue among themselves. Concatenate them at the end.

## Reference

```python
from collections import deque

def serving_order(arrivals):
    vips = deque()
    others = deque()
    for name, is_vip in arrivals:
        if is_vip:
            vips.append(name)
        else:
            others.append(name)
    return list(vips) + list(others)
```
