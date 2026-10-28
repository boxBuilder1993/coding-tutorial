# k-th smallest in a search tree

Write `kth_smallest(root, k)` that returns the `k`-th smallest value in a binary search
tree, with `k = 1` the smallest. `k` is at most the number of nodes.

```static
kth_smallest([3, 1, 4, None, 2], 1)  ->  1
kth_smallest([5, 3, 6, 2, 4, None, None, 1], 3)  ->  3
```

The point is to practise stopping an in-order traversal early.

## Starter

```python
def kth_smallest(root, k):
    ...
```

## Hints

1. In-order visits values in sorted order, so the `k`-th visited is the answer.
2. With the explicit-stack in-order loop, count pops and return at the `k`-th rather than collecting everything.

## Approach

In-order traversal with an early exit. Cost is the depth plus `k` steps rather than the whole tree.

## Reference

```python
def kth_smallest(root, k):
    stack = []
    node = root
    while True:
        while node is not None:
            stack.append(node)
            node = node.left
        node = stack.pop()
        k -= 1
        if k == 0:
            return node.val
        node = node.right
```
