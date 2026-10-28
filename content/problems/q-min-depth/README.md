# Shortest path to a leaf

Write `min_depth(root)` that returns the number of nodes on the shortest path from the
root to any leaf. An empty tree has depth 0. Note a node with one child is not a leaf.

```static
min_depth([3, 9, 20, None, None, 15, 7])  ->  2
min_depth([2, None, 3, None, 4])          ->  3
min_depth(None)                           ->  0
```

The point is to practise a recursion where a missing child must not be counted as a path.

## Starter

```python
def min_depth(root):
    ...
```

## Hints

1. A leaf returns 1. A node with only one child returns `1 + min_depth(that child)`.
2. A node with two children returns `1 + min(...)` of both. Taking `min` with a missing child would wrongly give 1.

## Approach

Like height but with `min`, and with care for one-child nodes: the missing side is not a route to a leaf. Linear.

## Reference

```python
def min_depth(root):
    if root is None:
        return 0
    if root.left is None:
        return 1 + min_depth(root.right)
    if root.right is None:
        return 1 + min_depth(root.left)
    return 1 + min(min_depth(root.left), min_depth(root.right))
```
