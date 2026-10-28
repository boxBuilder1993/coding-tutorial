# Lowest common ancestor in a search tree

`root` is a binary search tree containing both `a` and `b`. Write `lca(root, a, b)` that
returns the value of their lowest common ancestor: the deepest node that has both among
its descendants (a node counts as its own descendant).

```static
lca([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 8)  ->  6
lca([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 4)  ->  2
lca([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 3, 5)  ->  4
```

The point is to practise using the BST rule to walk down without searching both sides.

## Starter

```python
def lca(root, a, b):
    ...
```

## Hints

1. If both values are less than the node, go left; if both are greater, go right.
2. Otherwise the values are on different sides (or one is the node itself): this node is the answer.

## Approach

The split point, where the two targets go different ways, is the lowest common ancestor. A loop down the tree, as many steps as the tree is tall.

## Reference

```python
def lca(root, a, b):
    node = root
    while node is not None:
        if a < node.val and b < node.val:
            node = node.left
        elif a > node.val and b > node.val:
            node = node.right
        else:
            return node.val
```
