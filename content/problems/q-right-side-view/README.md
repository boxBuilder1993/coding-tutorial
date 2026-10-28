# Seen from the right

Write `right_view(root)` that returns the values you would see looking at the tree from
the right: the last node on each level, top to bottom.

```static
right_view([1, 2, 3, None, 5, None, 4])  ->  [1, 3, 4]
right_view([1, 2])                       ->  [1, 2]
right_view(None)                         ->  []
```

The point is to practise level-order traversal where only one node per level is kept.

## Starter

```python
def right_view(root):
    ...
```

## Hints

1. Level order with a queue; for each level, record the value of the last node popped.
2. Or depth-first visiting right before left, recording the first node seen at each new depth.

## Approach

A level at a time, keep the last. Linear.

## Reference

```python
from collections import deque

def right_view(root):
    if root is None:
        return []
    out = []
    queue = deque([root])
    while queue:
        for i in range(len(queue)):
            node = queue.popleft()
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        out.append(node.val)
    return out
```
