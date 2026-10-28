# Count the nodes

Write `count(root)` that returns how many nodes a binary tree has. An empty tree has 0.

```static
count([8, 3, 10, 1, 6, None, 14])  ->  6
count(None)                        ->  0
```

The point is to practise the basic tree recursion.

## Starter

```python
def count(root):
    ...
```

## Hints

1. `None` is 0.
2. Otherwise `1 + count(left) + count(right)`.

## Approach

The outline every tree recursion follows: base case for the empty tree, combine the two subtrees.

## Reference

```python
def count(root):
    if root is None:
        return 0
    return 1 + count(root.left) + count(root.right)
```
