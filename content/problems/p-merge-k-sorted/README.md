# Merge several sorted lists

Merging two sorted lists uses two positions. For many lists, a heap keeps
track of which list currently has the smallest front item. Push one entry
per list: `(first value, list number, 0)`. Repeatedly pop the smallest,
add its value to the result, and if that list has a next item, push
`(next value, list number, position + 1)`. Stop when the heap is empty.

Write `merge_all(lists)` that returns one sorted list containing every
item from every list. Lists may be empty. Do not use `sort` or `sorted`.

```static
merge_all([[1, 4, 9], [2, 3], [], [5]])  ->  [1, 2, 3, 4, 5, 9]
```

## Starter

```python
import heapq

def merge_all(lists):
    ...
```

## Hints

1. Seed the heap with the first item of each non-empty list, tagged with which list and which position.
2. After popping `(value, li, pos)`: if `pos + 1 < len(lists[li])`, push the next item from that list.

## Approach

The heap never holds more than one entry per list, and its smallest is always the overall smallest remaining item. The list number in the tuple breaks ties so that unequal values are never compared with each other.

## Reference

```python
import heapq

def merge_all(lists):
    heap = []
    for li, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], li, 0))
    result = []
    while heap:
        value, li, pos = heapq.heappop(heap)
        result.append(value)
        if pos + 1 < len(lists[li]):
            heapq.heappush(heap, (lists[li][pos + 1], li, pos + 1))
    return result
```
