# Largest value in a tree

Write `largest(root)` that returns the largest value in a non-empty binary tree. The tree
is not necessarily a search tree.

```static
largest([8, 3, 10, 1, 6, None, 14])  ->  14
largest([5])                         ->  5
```

The point is to practise a recursion that combines with `max`.

## Starter

```python
def largest(root):
    ...
```

## Hints

1. Return the max of the node's value and the largest of each non-empty child.
2. Let `None` return negative infinity, `float("-inf")`, so `max` ignores it.

## Approach

Each node reports the largest of itself and its subtrees. Linear.

## Reference

```python
def largest(root):
    if root is None:
        return float("-inf")
    return max(root.val, largest(root.left), largest(root.right))
```
