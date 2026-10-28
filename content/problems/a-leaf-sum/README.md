# Sum of the leaves

Write `leaf_sum(root)` that returns the sum of the values of all leaves,
the nodes with no children. An empty tree sums to `0`.

```static
leaf_sum([8, 3, 10, 1, 6, None, 14])  ->  21     (1 + 6 + 14)
leaf_sum([5])                         ->  5
leaf_sum(None)                        ->  0
```

The point is to practise a recursion with two base cases: the empty tree
and a leaf.

## Starter

```python
def leaf_sum(root):
    ...
```

## Hints

1. `None` returns `0`. A node with `left` and `right` both `None` returns its own `val`.
2. Anything else returns `leaf_sum(root.left) + leaf_sum(root.right)`.

## Approach

Three cases: empty, leaf, internal node. Only leaves contribute their value; internal nodes just pass the question down.

## Reference

```python
def leaf_sum(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return root.val
    return leaf_sum(root.left) + leaf_sum(root.right)
```
