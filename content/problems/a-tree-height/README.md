# Height of a tree

Write `height(root)` that returns the number of nodes on the longest path
from the root down to a leaf. An empty tree (`None`) has height `0`; a
single node has height `1`. `root` is a `TreeNode` with `val`, `left` and
`right`.

```static
height([8, 3, 10, 1, 6, None, 14])  ->  3
height([1])                         ->  1
height(None)                        ->  0
```

The point is to practise recursion on trees.

## Starter

```python
def height(root):
    ...
```

## Hints

1. Base case: `if root is None: return 0`.
2. Otherwise `1 + max(height(root.left), height(root.right))`.

## Approach

The height of a tree is one more than the taller of its two subtrees, and the empty tree is zero. Two lines.

## Reference

```python
def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))
```
