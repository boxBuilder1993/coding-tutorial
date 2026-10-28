# Is it in the search tree?

`root` is a binary search tree: every value in a node's left subtree is
smaller than the node's value, every value in its right subtree is
larger. Write `contains(root, target)` that returns whether `target` is in
the tree.

```static
contains([8, 3, 10, 1, 6, None, 14], 6)  ->  True
contains([8, 3, 10, 1, 6, None, 14], 7)  ->  False
contains(None, 7)                        ->  False
```

The point is to practise using the BST rule: go left or right, never
both. One check uses a tree of a hundred thousand nodes.

## Starter

```python
def contains(root, target):
    ...
```

## Hints

1. A loop works as well as recursion: `node = root`, while `node is not None`.
2. If `target == node.val`, return `True`. If `target < node.val`, go to `node.left`; otherwise `node.right`.
3. Falling off the tree means it is not there.

## Approach

Binary search on a tree: each comparison discards a whole subtree. The number of steps is the height of the tree.

## Reference

```python
def contains(root, target):
    node = root
    while node is not None:
        if target == node.val:
            return True
        node = node.left if target < node.val else node.right
    return False
```
