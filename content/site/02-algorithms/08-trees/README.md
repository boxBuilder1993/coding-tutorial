---
title: Binary trees in Python: recursion, depth-first and breadth-first traversal, BSTs
description: Tree nodes, computing height and sums by recursion, pre-, in- and post-order traversal, level order with a queue, and binary search trees.
---
# Trees

A linked list node points to one next node. Let it point to two, a left
and a right, and you have a **binary tree**. The node everything hangs from
is the root; nodes with no children are leaves. Trees are the shape of
folders inside folders, of a tournament bracket, of the sorted structure
behind database indexes, and recursion fits them exactly, because every
child is itself the root of a smaller tree.

## A tree node

```python
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = Node(8, Node(3, Node(1), Node(6)), Node(10, None, Node(14)))
print(root.val, root.left.val, root.right.val)
print(root.right.left)
```

That builds this tree:

```static
        8
      /   \
     3     10
    / \      \
   1   6      14
```

The checker provides `TreeNode` with the same three fields, and describes
trees in exercises as a list in **level order**: the root, then the
second level left to right, then the third, with `None` for a missing
child. The tree above is `[8, 3, 10, 1, 6, None, 14]`.

## Recursion on trees

Every tree question has the same recursive shape: an empty tree (`None`)
is the base case, and the answer for a node combines the answers for its
left and right subtrees.

```python
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = Node(8, Node(3, Node(1), Node(6)), Node(10, None, Node(14)))

def count(node):
    if node is None:
        return 0
    return 1 + count(node.left) + count(node.right)

def total(node):
    if node is None:
        return 0
    return node.val + total(node.left) + total(node.right)

def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))

print(count(root), total(root), height(root))
```

Three functions, one outline. `height` counts nodes on the longest path
from the root down, so a single node has height 1 and an empty tree 0.
Each node is visited once, so all three are linear in the number of nodes.

Try writing `contains(node, target)`, `max_value(node)` and
`count_leaves(node)` in the block above before reading on. They are the
same outline with a different base case or combination.

## Depth first: three orders

Visiting every node by recursion is a **depth-first** traversal: it goes
all the way down the left before touching the right. Where you handle the
node's own value relative to its children gives three named orders.

```python
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = Node(8, Node(3, Node(1), Node(6)), Node(10, None, Node(14)))

def preorder(node, out):
    if node is None:
        return
    out.append(node.val)
    preorder(node.left, out)
    preorder(node.right, out)

def inorder(node, out):
    if node is None:
        return
    inorder(node.left, out)
    out.append(node.val)
    inorder(node.right, out)

def postorder(node, out):
    if node is None:
        return
    postorder(node.left, out)
    postorder(node.right, out)
    out.append(node.val)

for f in [preorder, inorder, postorder]:
    out = []
    f(root, out)
    print(f.__name__, out)
```

- **Pre-order**, node first: copying a tree, or printing a folder tree
  with the folder name above its contents.
- **In-order**, node between: on a binary search tree this produces the
  values sorted, as above.
- **Post-order**, node last: deleting a tree, or computing sizes where a
  folder's size needs its contents' sizes first.

`out` is passed in and appended to, which avoids building and joining
lists at every level. Returning `left + [node.val] + right` also works and
reads well; it costs extra copying.

## Breadth first: level by level

To visit the tree a level at a time, recursion is the wrong tool; use a
queue. Put the root in. Repeatedly take the front node, record it, and put
its children at the back. Children always queue up behind everything on
their parent's level, so levels come out in order.

```python
from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = Node(8, Node(3, Node(1), Node(6)), Node(10, None, Node(14)))

def level_order(root):
    if root is None:
        return []
    out = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        out.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return out

print(level_order(root))
```

This is the **breadth-first search** from [Module 4](../../01-learn-python/04-stacks-queues-and-priority-queues/02-queues),
and the same loop works on graphs on the next page. To get the levels as
separate lists, note `len(queue)` at the start of each round and pop
exactly that many nodes before starting the next list.

The depth-first orders can also be done without recursion by using an
explicit stack instead of the queue; swapping `deque` for a list with
`pop()` turns `level_order` into a pre-order traversal (with right pushed
before left). Recursion is just that stack kept for you.

## Binary search trees

A **binary search tree** (BST) keeps a rule: every value in a node's left
subtree is smaller than the node, every value in its right subtree is
larger. The example tree is one. The rule makes searching a binary search:
compare with the node, go left or right, never both.

```python
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = Node(8, Node(3, Node(1), Node(6)), Node(10, None, Node(14)))

def contains(node, target):
    while node is not None:
        if target == node.val:
            return True
        node = node.left if target < node.val else node.right
    return False

def insert(node, val):
    if node is None:
        return Node(val)
    if val < node.val:
        node.left = insert(node.left, val)
    else:
        node.right = insert(node.right, val)
    return node

print(contains(root, 6), contains(root, 7))
insert(root, 7)
print(contains(root, 7), root.left.right.right.val)
```

Search and insert take as many steps as the tree is tall. For a
balanced tree that is log n, which is why sorted structures in databases
and language runtimes are trees. Insert values in sorted order, though,
and every node goes right: the tree becomes a linked list and the
advantage is gone. Self-balancing trees fix that and are beyond this
course; Python's `sorted` list plus `bisect` covers most needs.

Validating a BST is a common question. The trap: checking each node
against only its children is not enough; every node must sit within the
range allowed by all its ancestors. Pass the allowed `(low, high)` down
the recursion.

## Try it

Trees in the exercises arrive as `TreeNode` objects built from level-order
lists, or `None` for an empty tree. Where you return a tree, the checker
reads it back in level order.

:::problem a-tree-height

:::problem a-leaf-sum

:::problem a-levels

:::problem a-bst-contains

:::problem a-mirror-tree

Next: [Graphs](../09-graphs).
