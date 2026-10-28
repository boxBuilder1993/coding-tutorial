# Is there a path with this sum?

Write `has_path_sum(root, target)` that returns whether some path from the root to a leaf
has values adding up to `target`. An empty tree has no paths.

```static
has_path_sum([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 22)  ->  True   (5+4+11+2)
has_path_sum([1, 2, 3], 5)  ->  False
has_path_sum(None, 0)       ->  False
```

The point is to practise passing a shrinking target down the recursion and recognising
leaves.

## Starter

```python
def has_path_sum(root, target):
    ...
```

## Hints

1. At a leaf, the answer is `target == root.val`.
2. Otherwise subtract the value and ask either child; `None` children return `False`.

## Approach

Each step reduces the target by the node's value; a leaf checks whether exactly its value is left. Linear.

## Reference

```python
def has_path_sum(root, target):
    if root is None:
        return False
    if root.left is None and root.right is None:
        return target == root.val
    rest = target - root.val
    return has_path_sum(root.left, rest) or has_path_sum(root.right, rest)
```
