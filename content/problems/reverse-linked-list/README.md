# Reverse Linked List

Given the head of a singly linked list, reverse it and return the new head.
Nodes have `.val` and `.next`. Import `ListNode` from `checker` if you need
to build nodes; the tests build lists for you.

```static
1 -> 2 -> 3 -> 4 -> 5   becomes   5 -> 4 -> 3 -> 2 -> 1
```

## Starter

```python
def reverse_list(head):
    ...
```

## Hints

1. Keep `prev` and `curr`. Save `curr.next` before you overwrite it.
2. When `curr` becomes `None`, `prev` is the new head.

## Approach

Iterate with `prev = None`. For each node: save `nxt = curr.next`, point
`curr.next = prev`, then advance both. Time O(n), space O(1).

## Reference

```python
def reverse_list(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev, curr = curr, nxt
    return prev
```
