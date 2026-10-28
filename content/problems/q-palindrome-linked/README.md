# Is the list a palindrome?

Write `is_palindrome(head)` that returns whether the linked list reads the same forwards
and backwards.

```static
is_palindrome(1 -> 2 -> 2 -> 1)  ->  True
is_palindrome(1 -> 2)            ->  False
is_palindrome(None)              ->  True
```

The point is to practise combining the techniques: find the middle, reverse the second
half, compare. Reading the values into a Python list also passes.

## Starter

```python
def is_palindrome(head):
    ...
```

## Hints

1. Simple way: collect the values into a list and compare it with its reverse.
2. Constant-space way: fast/slow to the middle, reverse from the middle, then walk both halves comparing values.

## Approach

Either approach is linear. The in-place version is what interviews mean by the question; the list version is what you would write in practice.

## Reference

```python
def is_palindrome(head):
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    prev = None
    while slow is not None:
        nxt = slow.next
        slow.next = prev
        prev = slow
        slow = nxt
    left, right = head, prev
    while right is not None:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    return True
```
