# Rebuild a tree from two traversals

Write `build(preorder, inorder)` that returns the root of the binary tree whose pre-order
and in-order traversals are the two given lists. Values are distinct. Import `TreeNode`
from `checker`.

```static
build([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])  ->  the tree [3, 9, 20, None, None, 15, 7]
build([], [])                                ->  None
```

The first pre-order value is the root; its position in the in-order list splits the rest
into left and right subtrees. A dictionary from value to in-order index keeps it linear.

## Starter

```python
def build(preorder, inorder):
    ...
```

## Hints

1. `index = {v: i for i, v in enumerate(inorder)}`. Consume pre-order values in order with a running pointer.
2. `go(lo, hi)` builds the subtree whose in-order range is `inorder[lo:hi]`: if empty return `None`; root is the next pre-order value; left is `go(lo, index[root])`, right is `go(index[root] + 1, hi)`.
3. Build left before right, because pre-order lists the left subtree first.

## Approach

Pre-order gives roots top-down, in-order tells how many nodes go left. With the index map each node is placed in constant time. Linear.

## Reference

```python
from checker import TreeNode

def build(preorder, inorder):
    index = {v: i for i, v in enumerate(inorder)}
    pos = [0]

    def go(lo, hi):
        if lo >= hi:
            return None
        val = preorder[pos[0]]
        pos[0] += 1
        node = TreeNode(val)
        node.left = go(lo, index[val])
        node.right = go(index[val] + 1, hi)
        return node

    return go(0, len(inorder))
```
