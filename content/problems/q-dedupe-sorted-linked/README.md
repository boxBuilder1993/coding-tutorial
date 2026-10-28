# Remove duplicates from a sorted linked list

Write `dedupe(head)` that removes repeated values from a sorted linked list so each value
appears once, relinking the existing nodes, and returns the head.

```static
dedupe(1 -> 1 -> 2 -> 3 -> 3)  ->  1 -> 2 -> 3
dedupe(None)                   ->  None
```

The point is to practise comparing a node with its successor and skipping.

## Starter

```python
def dedupe(head):
    ...
```

## Hints

1. Walk with `current`. If `current.next` has the same value, set `current.next = current.next.next` and stay put.
2. Otherwise advance. Stop when `current` or `current.next` is `None`.

## Approach

Because the list is sorted, duplicates are adjacent. Skip a successor that matches; move on when it does not. Linear.

## Reference

```python
def dedupe(head):
    current = head
    while current is not None and current.next is not None:
        if current.next.val == current.val:
            current.next = current.next.next
        else:
            current = current.next
    return head
```
