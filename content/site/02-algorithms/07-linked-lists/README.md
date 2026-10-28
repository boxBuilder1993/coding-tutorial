---
title: Linked lists in Python: nodes, pointers, reversal and the two-pointer tricks
description: Build a linked list from node objects, walk it, insert and delete by relinking, reverse it, use a dummy head, and find the middle with fast and slow pointers.
---
# Linked lists

A Python list stores its items side by side, which is why indexing is one
step and inserting at the front means shifting everything. A **linked
list** stores each item in its own small box, called a node, that holds
the value and a reference to the next box. Nothing is side by side;
there is only "the first node" and each node knowing the next.

## A node

A node needs two names bundled together: `val` and `next`. Python bundles
names with a `class`. This course has avoided classes, and will keep
doing so beyond this minimal use: a class here is only a way to make a
value with named parts.

```python
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

a = Node("apple")
b = Node("bread")
a.next = b
print(a.val, "->", a.next.val)
print(b.next)
```

`Node("apple")` makes a node; `a.val` and `a.next` read its parts; `a.next = b`
links it to another. The last node's `next` is `None`, which is how you
know the list has ended. That is all the class does.

In the exercises, the checker provides this class under the name
`ListNode`, with the same two fields, and builds lists for you. Import it
when you need to make new nodes:

```python static
from checker import ListNode
node = ListNode(5)
```

## Walking the list

The whole list is reachable from its first node, the **head**. To visit
every node, keep a `current` reference and move it along `next` until it
falls off the end:

```python
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

head = Node("apple", Node("bread", Node("milk")))

current = head
while current is not None:
    print(current.val)
    current = current.next
```

This loop is to linked lists what `for item in items` is to Python lists,
and every algorithm on this page is built from it. Length, search, sum: all
one walk, all linear. There is no indexing: `the third item` means
walking three steps.

## Insert and delete by relinking

Inserting at the front is one step however long the list is: make a node
whose `next` is the old head, and call it the new head. Compare
`items.insert(0, x)` on a Python list, which shifts every item.

```python
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def to_list(head):
    out = []
    while head is not None:
        out.append(head.val)
        head = head.next
    return out

head = Node("bread", Node("milk"))
head = Node("apple", head)
print(to_list(head))
```

Deleting a node means making the node before it skip over it. You need
to be standing on the previous node, so walk until `current.next` is the
one to remove:

```python
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def to_list(head):
    out = []
    while head is not None:
        out.append(head.val)
        head = head.next
    return out

head = Node("apple", Node("bread", Node("milk")))
current = head
while current.next is not None and current.next.val != "bread":
    current = current.next
if current.next is not None:
    current.next = current.next.next
print(to_list(head))
```

Nothing moves. One reference changes and `bread` is no longer reachable.
This is the one thing a linked list does better than a Python list:
insert or delete next to a node you are already holding, in constant
time.

## The dummy head

Deleting the first node is a special case in the code above, because
there is no node before it. The standard fix is a **dummy** node placed in
front of the head, so every real node has a predecessor. Return
`dummy.next` at the end.

```python
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def to_list(head):
    out = []
    while head is not None:
        out.append(head.val)
        head = head.next
    return out

def remove_all(head, target):
    dummy = Node(None, head)
    current = dummy
    while current.next is not None:
        if current.next.val == target:
            current.next = current.next.next
        else:
            current = current.next
    return dummy.next

head = Node(1, Node(2, Node(1, Node(3, Node(1)))))
print(to_list(remove_all(head, 1)))
```

Note that after a removal `current` stays put, because the new
`current.next` has not been examined yet. The dummy head appears in
nearly every linked-list solution; reach for it whenever the head might
change.

## Reversing

Reverse the list by walking it and pointing each node at the one before
it. Three references: the previous node, the current one, and the next one
saved before the link is overwritten.

```python
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def to_list(head):
    out = []
    while head is not None:
        out.append(head.val)
        head = head.next
    return out

def reverse(head):
    prev = None
    current = head
    while current is not None:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev

head = Node(1, Node(2, Node(3, Node(4))))
print(to_list(reverse(head)))
```

Saving `nxt` first is the step people forget: once `current.next = prev`
runs, the old next is gone. At the end `current` is `None` and `prev` is
the last node visited, which is the new head. This is the most asked
linked-list question in interviews; write it until it is automatic.

## Fast and slow pointers

Finding the middle without counting: move one reference one step at a
time and another two steps. When the fast one reaches the end, the slow
one is halfway.

```python
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def middle(head):
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow

head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(middle(head).val)
head = Node(1, Node(2, Node(3, Node(4))))
print(middle(head).val)
```

With an even count this returns the second of the two middle nodes. The
same two pointers detect a cycle: if the list loops back on itself, the
fast pointer eventually laps the slow one and they meet; if there is no
cycle, fast reaches `None`.

## Why bother, when Python has lists

In Python you will rarely build a linked list yourself; `deque` is one
underneath, and a plain list is faster for almost everything. The reasons
to learn them anyway: they are the simplest structure made of references,
which trees and graphs also are; constant-time insertion next to a held
node is sometimes exactly what is needed; and interviews ask about them
constantly because the pointer manipulation reveals whether you can hold
a few references in your head.

## Try it

In the exercises `head` is a `ListNode` built by the checker, or `None`
for an empty list. Results are compared by reading the list back out, so
return the head node of your answer.

:::problem a-list-length

:::problem a-reverse-linked-list

:::problem a-middle-node

:::problem a-remove-value

:::problem a-merge-sorted-linked

Next: [Trees](../08-trees).
