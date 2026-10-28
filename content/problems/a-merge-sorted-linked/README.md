# Merge two sorted linked lists

`a` and `b` are the heads of two linked lists whose values are in
ascending order. Write `merge(a, b)` that returns the head of one sorted
linked list containing all the nodes from both. Either input may be
`None`.

```static
merge(1 -> 3 -> 5, 2 -> 3 -> 6)  ->  1 -> 2 -> 3 -> 3 -> 5 -> 6
merge(None, 4 -> 7)              ->  4 -> 7
```

The point is to practise the merge step on nodes: relink the existing
nodes rather than copying values into a new list.

## Starter

```python
def merge(a, b):
    ...
```

## Hints

1. Start with a dummy node and a `tail` reference pointing at it.
2. While both `a` and `b` are not `None`, attach the smaller head to `tail.next`, advance that list and move `tail` forward.
3. When one runs out, attach whatever is left of the other: `tail.next = a if a is not None else b`. Return `dummy.next`.

## Approach

Exactly the list merge from the sorting page, with `tail.next = node` in place of `append`. The dummy head means no special case for which list supplies the first node.

## Reference

```python
from checker import ListNode

def merge(a, b):
    dummy = ListNode()
    tail = dummy
    while a is not None and b is not None:
        if a.val <= b.val:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
        tail = tail.next
    tail.next = a if a is not None else b
    return dummy.next
```
