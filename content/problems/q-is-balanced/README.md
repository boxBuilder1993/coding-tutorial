# Is the tree balanced?

A binary tree is height-balanced if, at every node, the heights of the left and right
subtrees differ by at most one. Write `is_balanced(root)`.

```static
is_balanced([3, 9, 20, None, None, 15, 7])  ->  True
is_balanced([1, 2, 2, 3, 3, None, None, 4, 4])  ->  False
is_balanced(None)                           ->  True
```

The point is to practise a recursion that returns extra information upward so each node
is visited once: return the height, or a sentinel meaning "unbalanced below".

## Starter

```python
def is_balanced(root):
    ...
```

## Hints

1. Write `height(node)` that returns -1 if the subtree is unbalanced, else its height.
2. If either child returns -1, or the two heights differ by more than 1, return -1; else `1 + max`.
3. `is_balanced` is `height(root) != -1`.

## Approach

Computing height at every node separately is quadratic. Returning the height and a failure signal together makes it one pass. Linear.

## Reference

```python
def is_balanced(root):
    def height(node):
        if node is None:
            return 0
        left = height(node.left)
        if left == -1:
            return -1
        right = height(node.right)
        if right == -1 or abs(left - right) > 1:
            return -1
        return 1 + max(left, right)

    return height(root) != -1
```
