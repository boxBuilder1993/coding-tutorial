# Partition around a value

Write `partition(head, x)` that rearranges the linked list so every node with a value
less than `x` comes before every node with a value at least `x`, preserving the original
order within each group, and returns the head.

```static
partition(1 -> 4 -> 3 -> 2 -> 5 -> 2, 3)  ->  1 -> 2 -> 2 -> 4 -> 3 -> 5
partition(2 -> 1, 2)                      ->  1 -> 2
```

The point is to practise building two lists with two tails and joining them.

## Starter

```python
def partition(head, x):
    ...
```

## Hints

1. Two dummy heads, `small` and `large`, each with a tail. Walk the list appending each node to the right tail.
2. At the end, set the large tail's `next` to `None`, join `small_tail.next = large.next`, return `small.next`.

## Approach

Splitting into two ordered lists and joining them keeps relative order and is linear. Terminating the large list is the step people forget, which leaves a cycle.

## Reference

```python
from checker import ListNode

def partition(head, x):
    small = ListNode()
    large = ListNode()
    s, l = small, large
    current = head
    while current is not None:
        if current.val < x:
            s.next = current
            s = s.next
        else:
            l.next = current
            l = l.next
        current = current.next
    l.next = None
    s.next = large.next
    return small.next
```
