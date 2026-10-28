# Serialize and rebuild a tree

Write two functions: `serialize(root)` that turns a binary tree into a string, and
`deserialize(text)` that turns that string back into an identical tree. Any format works
as long as the round trip reproduces the tree exactly, including `None` for an empty tree.

```static
deserialize(serialize(tree))  ->  a tree with the same shape and values
```

Pre-order with a marker for missing children is the usual choice: write `val` then the
left subtree then the right, and `#` for `None`. Rebuilding consumes the tokens in the
same order with recursion. Import `TreeNode` from `checker`.

## Starter

```python
def serialize(root):
    ...

def deserialize(text):
    ...
```

## Hints

1. Serialize: pre-order into a list of tokens, `"#"` for `None`, then `",".join`.
2. Deserialize: split into tokens, keep an index (or use an iterator with `next`), and write `build()` that reads one token: `#` returns `None`, otherwise makes a node and recursively builds left then right.
3. Values can be negative or multi-digit, so split on the separator rather than reading character by character.

## Approach

Pre-order with explicit null markers is unambiguous, so no second traversal is needed. Both directions are linear.

## Reference

```python
from checker import TreeNode

def serialize(root):
    out = []
    def go(node):
        if node is None:
            out.append("#")
            return
        out.append(str(node.val))
        go(node.left)
        go(node.right)
    go(root)
    return ",".join(out)

def deserialize(text):
    tokens = iter(text.split(","))
    def build():
        tok = next(tokens)
        if tok == "#":
            return None
        node = TreeNode(int(tok))
        node.left = build()
        node.right = build()
        return node
    return build()
```
