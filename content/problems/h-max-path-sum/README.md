# Largest path sum in a tree

A path is any sequence of nodes where each is a parent or child of the next, with no node
repeated; it need not pass through the root or end at a leaf. Write `max_path_sum(root)`
that returns the largest sum of values along any path in a non-empty binary tree.

```static
max_path_sum([1, 2, 3])                            ->  6
max_path_sum([-10, 9, 20, None, None, 15, 7])      ->  42     (15 + 20 + 7)
max_path_sum([-3])                                 ->  -3
```

At each node, the best path *through* it is `val + best downward left + best downward
right`, where a negative downward contribution is replaced by zero. The function returns
the best downward path (one side only) to its parent while updating a global best.

## Starter

```python
def max_path_sum(root):
    ...
```

## Hints

1. Inner `down(node)` returns the best sum of a path that starts at `node` and goes down one side, never negative: `max(0, ...)` on each child.
2. Inside it, update `best` with `node.val + left_down + right_down`.
3. Use `nonlocal best` or a one-element list to update the outer variable.

## Approach

Post-order recursion that reports one-sided gains upward and checks two-sided totals at each node. Linear.

## Reference

```python
def max_path_sum(root):
    best = float("-inf")

    def down(node):
        nonlocal best
        if node is None:
            return 0
        left = max(0, down(node.left))
        right = max(0, down(node.right))
        best = max(best, node.val + left + right)
        return node.val + max(left, right)

    down(root)
    return best
```
