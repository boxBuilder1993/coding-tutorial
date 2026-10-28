# Are two trees the same?

Write `same(a, b)` that returns whether two binary trees have the same shape and the
same values in the same places.

```static
same([1, 2, 3], [1, 2, 3])        ->  True
same([1, 2], [1, None, 2])        ->  False
same(None, None)                  ->  True
```

The point is to practise recursing over two trees in step.

## Starter

```python
def same(a, b):
    ...
```

## Hints

1. Both `None`: `True`. One `None`: `False`.
2. Otherwise values equal and `same` on both pairs of children.

## Approach

Compare the roots, then the left subtrees, then the right subtrees. Stops early on the first difference.

## Reference

```python
def same(a, b):
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    return a.val == b.val and same(a.left, b.left) and same(a.right, b.right)
```
