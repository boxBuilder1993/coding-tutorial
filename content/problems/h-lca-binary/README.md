# Lowest common ancestor in any binary tree

`root` is a binary tree (not necessarily a search tree) with distinct values that contains
both `a` and `b`. Write `lca(root, a, b)` that returns the value of their lowest common
ancestor.

```static
lca([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 1)  ->  3
lca([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 4)  ->  5
lca([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 7, 4)  ->  2
```

Without the search-tree rule you cannot steer; recurse into both sides and let each
subtree report whether it contains one of the targets. The first node where both sides
report, or that is itself a target with the other below, is the answer.

## Starter

```python
def lca(root, a, b):
    ...
```

## Hints

1. `find(node)` returns `None` if neither target is in the subtree, the target node if exactly one is, and the LCA node once both have been found.
2. If `node` is a target, return `node` immediately (the other, if below, makes this the LCA anyway). Otherwise get `left = find(node.left)`, `right = find(node.right)`: both non-`None` means `node` is the LCA; else return whichever is non-`None`.

## Approach

One post-order pass returning a node up the tree; the point where two non-empty results meet is the lowest common ancestor. Linear.

## Reference

```python
def lca(root, a, b):
    def find(node):
        if node is None:
            return None
        if node.val == a or node.val == b:
            return node
        left = find(node.left)
        right = find(node.right)
        if left is not None and right is not None:
            return node
        return left if left is not None else right

    return find(root).val
```
