# Values by level

Write `levels(root)` that returns a list of lists: the values on each
level of the tree from top to bottom, each level left to right. An empty
tree gives `[]`.

```static
levels([8, 3, 10, 1, 6, None, 14])  ->  [[8], [3, 10], [1, 6, 14]]
levels([1])                         ->  [[1]]
```

The point is to practise breadth-first traversal with a queue, one level
at a time.

## Starter

```python
def levels(root):
    ...
```

## Hints

1. `from collections import deque`; start the queue with the root (unless it is `None`).
2. Each round, note `count = len(queue)` and pop exactly that many nodes into one list, appending children as you go.
3. Append that list to the result; stop when the queue is empty.

## Approach

Level order with a twist: everything in the queue at the start of a round is exactly one level, so popping that many nodes separates the levels. Children appended during the round form the next level.

## Reference

```python
from collections import deque

def levels(root):
    if root is None:
        return []
    out = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        out.append(level)
    return out
```
