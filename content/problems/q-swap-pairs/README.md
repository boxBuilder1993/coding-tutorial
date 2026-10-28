# Swap nodes in pairs

Write `swap_pairs(head)` that swaps every two adjacent nodes, relinking rather than
changing values, and returns the new head. A leftover node at the end stays put.

```static
swap_pairs(1 -> 2 -> 3 -> 4)  ->  2 -> 1 -> 4 -> 3
swap_pairs(1 -> 2 -> 3)       ->  2 -> 1 -> 3
swap_pairs(None)              ->  None
```

The point is to practise relinking three nodes at a time with a dummy head.

## Starter

```python
def swap_pairs(head):
    ...
```

## Hints

1. Dummy head; `prev = dummy`. While `prev.next` and `prev.next.next` exist, name them `first` and `second`.
2. Relink: `first.next = second.next`, `second.next = first`, `prev.next = second`. Then `prev = first`.

## Approach

Each step rewires three links so the pair is reversed, then moves on past the pair. Linear.

## Reference

```python
from checker import ListNode

def swap_pairs(head):
    dummy = ListNode(None, head)
    prev = dummy
    while prev.next is not None and prev.next.next is not None:
        first = prev.next
        second = first.next
        first.next = second.next
        second.next = first
        prev.next = second
        prev = first
    return dummy.next
```
