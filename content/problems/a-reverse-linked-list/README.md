# Reverse a linked list

Write `reverse(head)` that reverses the linked list in place by
re-pointing each node's `next`, and returns the new head. `head` is a
`ListNode` or `None`.

```static
reverse(1 -> 2 -> 3 -> 4)  ->  4 -> 3 -> 2 -> 1
reverse(None)              ->  None
```

The point is to practise pointer manipulation with three references:
previous, current and next. Relink the existing nodes rather than
building a new list.

## Starter

```python
def reverse(head):
    ...
```

## Hints

1. `prev = None`, `current = head`. Loop while `current is not None`.
2. Save `nxt = current.next` first, then `current.next = prev`, then advance both: `prev = current`, `current = nxt`.
3. When the loop ends, `prev` is the new head.

## Approach

Walk the list once. At each node, remember where it pointed, point it backwards at the previous node, and step forward using the remembered reference. The last node seen is the new head.

## Reference

```python
def reverse(head):
    prev = None
    current = head
    while current is not None:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev
```
