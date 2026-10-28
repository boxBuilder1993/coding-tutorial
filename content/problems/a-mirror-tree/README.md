# Mirror a tree

Write `mirror(root)` that swaps the left and right children of every
node, so the tree becomes its mirror image, and returns the root. Change
the tree in place.

```static
mirror([8, 3, 10, 1, 6, None, 14])  ->  [8, 10, 3, 14, None, 6, 1]
mirror(None)                        ->  None
```

The point is to practise a recursion that changes the tree rather than
computing a number from it.

## Starter

```python
def mirror(root):
    ...
```

## Hints

1. Base case: `None` returns `None`.
2. Swap: `root.left, root.right = root.right, root.left`.
3. Then mirror both children with recursive calls, and return `root`.

## Approach

Swap the two children at this node, then recurse into each. The order of swap and recursion does not matter as long as both children are mirrored. Every node is visited once.

## Reference

```python
def mirror(root):
    if root is None:
        return None
    root.left, root.right = root.right, root.left
    mirror(root.left)
    mirror(root.right)
    return root
```
