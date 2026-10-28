# Order the tasks

`prereqs` is a dictionary from each task to the list of tasks that must be done before it.
Every task is a key, and there are no circular requirements. Write `task_order(prereqs)`
that returns a list of all tasks in an order where every task comes after its prerequisites.
Any valid order passes.

```static
task_order({"wake": [], "dress": ["wake"], "eat": ["wake"], "leave": ["dress", "eat"]})
    ->  ["wake", "dress", "eat", "leave"]    (or ["wake", "eat", "dress", "leave"])
```

The point is to practise topological sorting: repeatedly take a task with no remaining
prerequisites.

## Starter

```python
def task_order(prereqs):
    ...
```

## Hints

1. Count remaining prerequisites per task, and build the reverse map: for each prerequisite, which tasks it unlocks.
2. Queue every task with count 0. Pop, append to the order, and decrement the count of each task it unlocks; queue those that hit 0.
3. This is Kahn's algorithm. A DFS that appends after visiting all prerequisites also works.

## Approach

Tasks with nothing outstanding can go first; finishing one may free others. A queue of ready tasks processes each once. Linear in tasks plus requirements.

## Reference

```python
from collections import deque

def task_order(prereqs):
    remaining = {t: len(ps) for t, ps in prereqs.items()}
    unlocks = {t: [] for t in prereqs}
    for t, ps in prereqs.items():
        for p in ps:
            unlocks[p].append(t)
    queue = deque(t for t, n in remaining.items() if n == 0)
    order = []
    while queue:
        t = queue.popleft()
        order.append(t)
        for nxt in unlocks[t]:
            remaining[nxt] -= 1
            if remaining[nxt] == 0:
                queue.append(nxt)
    return order
```
