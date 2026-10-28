# Join the ropes

You have ropes of the given lengths and must join them into one. Joining
two ropes costs the sum of their lengths and produces a rope of that
length. Write `join_cost(ropes)` that returns the minimum total cost of
joining them all. A single rope costs `0`.

```static
join_cost([4, 3, 2, 6])  ->  29     (2+3=5, 4+5=9, 6+9=15; 5 + 9 + 15 = 29)
join_cost([5])           ->  0
```

The point is to practise "repeatedly take the two smallest and put the
result back", which is what a heap is for.

## Starter

```python
def join_cost(ropes):
    ...
```

## Hints

1. `heapq.heapify` the list, then loop while it has more than one rope.
2. Pop two, add their sum to the total cost, push the sum back.
3. Always joining the two shortest first is what makes the total minimal: longer ropes get added fewer times.

## Approach

A heap gives the two smallest in log n each. Each join reduces the count by one, so there are `n - 1` joins, for n log n total. Taking the two smallest every time is the greedy choice that is correct here, for the same reason as Huffman coding.

## Reference

```python
import heapq

def join_cost(ropes):
    heap = list(ropes)
    heapq.heapify(heap)
    cost = 0
    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        cost += a + b
        heapq.heappush(heap, a + b)
    return cost
```
