# Is it a valid search tree?

Write `is_bst(root)` that returns whether the tree satisfies the binary search tree rule
everywhere: every value in a node's left subtree is strictly less than the node, every
value in its right subtree strictly greater.

```static
is_bst([2, 1, 3])                ->  True
is_bst([5, 1, 4, None, None, 3, 6])  ->  False    (3 is in the right subtree of 5)
is_bst(None)                     ->  True
```

The point is to practise passing allowed bounds down the recursion. Checking each node
against only its children misses the second example.

## Starter

```python
def is_bst(root):
    ...
```

## Hints

1. Inner function `ok(node, low, high)`: `None` is fine; otherwise `low < node.val < high` must hold.
2. Recurse left with `high = node.val` and right with `low = node.val`. Start with infinite bounds.
3. Alternative: the in-order values must be strictly increasing.

## Approach

Every node must fit inside the range set by all its ancestors, which the two bounds carry down. Linear.

## Reference

```python
def is_bst(root):
    def ok(node, low, high):
        if node is None:
            return True
        if not (low < node.val < high):
            return False
        return ok(node.left, low, node.val) and ok(node.right, node.val, high)

    return ok(root, float("-inf"), float("inf"))
```
