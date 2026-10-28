# Remove every occurrence

Write `remove_all(head, target)` that removes every node whose `val`
equals `target` from the linked list and returns the head of what
remains, which may be `None`.

```static
remove_all(1 -> 2 -> 1 -> 3 -> 1, 1)  ->  2 -> 3
remove_all(7 -> 7, 7)                 ->  None
remove_all(None, 7)                   ->  None
```

The point is to practise the dummy-head technique, so the head being
removed needs no special case.

## Starter

```python
def remove_all(head, target):
    ...
```

## Hints

1. Make a dummy node in front: `from checker import ListNode` then `dummy = ListNode(None, head)`.
2. Walk with `current = dummy` while `current.next is not None`. If `current.next.val == target`, skip it with `current.next = current.next.next`; otherwise advance `current`.
3. Return `dummy.next`.

## Approach

With a dummy node every real node has a predecessor, so removal is always "make the previous node skip this one". Do not advance after a removal, because the new `current.next` has not been checked yet.

## Reference

```python
from checker import ListNode

def remove_all(head, target):
    dummy = ListNode(None, head)
    current = dummy
    while current.next is not None:
        if current.next.val == target:
            current.next = current.next.next
        else:
            current = current.next
    return dummy.next
```
