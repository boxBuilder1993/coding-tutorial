# In-order values

Write `inorder(root)` that returns the values of a binary tree in in-order: left subtree,
node, right subtree. On a binary search tree this is sorted order.

```static
inorder([8, 3, 10, 1, 6, None, 14])  ->  [1, 3, 6, 8, 10, 14]
inorder(None)                        ->  []
```

The point is to practise a traversal that collects into a list, recursively or with an
explicit stack.

## Starter

```python
def inorder(root):
    ...
```

## Hints

1. Recursive: an inner function that recurses left, appends, recurses right.
2. Iterative: push nodes while going left; pop, record, then go right.

## Approach

Either form is linear. The explicit stack version is the one to know for 'without recursion' follow-ups.

## Reference

```python
def inorder(root):
    out = []
    stack = []
    node = root
    while stack or node is not None:
        while node is not None:
            stack.append(node)
            node = node.left
        node = stack.pop()
        out.append(node.val)
        node = node.right
    return out
```
