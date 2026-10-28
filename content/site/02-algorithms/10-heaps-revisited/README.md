---
title: Heaps in Python for top-k, k-th largest and merging: heapq patterns
description: Heap patterns beyond push and pop: a bounded heap for the top k, heaps of tuples, merging sorted streams, and two heaps for a running median.
---
# Heaps revisited

[Module 4](../../01-learn-python/04-stacks-queues-and-priority-queues/03-priority-queues)
introduced `heapq` as "always take the smallest". Now that cost has a
vocabulary: `heappush` and `heappop` each take about log n steps on a heap
of `n` items, and `heapify` turns a list into a heap in linear time. Those
two facts make a handful of patterns much faster than sorting.

## The top k, with a heap of size k

The five most expensive orders out of a million: sorting all million is
n log n. Keeping a heap of only five is n log 5, which is close to linear.
The trick is that the heap holds the **smallest** of the current top five
at its root, so one comparison tells you whether a new item belongs.

```python
import heapq

def top_k(items, k):
    heap = []
    for x in items:
        if len(heap) < k:
            heapq.heappush(heap, x)
        elif x > heap[0]:
            heapq.heapreplace(heap, x)
    return sorted(heap, reverse=True)

sales = [12, 3, 45, 7, 23, 56, 8, 31, 2, 19]
print(top_k(sales, 3))
print(heapq.nlargest(3, sales))
```

`heap[0]` is the smallest item in the heap without removing it.
`heapreplace` pops the smallest and pushes the new item in one step. A
min-heap finds the largest items because what it is good at is discarding
the smallest. `heapq.nlargest` does exactly this and is what you would
call in real code; the loop is what it does inside.

The k-th largest item is the root of that heap when the loop ends, which
also answers "the k-th largest in a stream" as items keep arriving.

## Heaps of tuples

A heap compares whole items, so to order records by one field put that
field first in a tuple. The practice problem [top k frequent](problem:p-top-k-frequent)
is a `Counter` followed by a heap of `(count, word)` tuples:

```python
import heapq
from collections import Counter

words = "the cat sat on the mat the cat ran".split()
counts = Counter(words)
print(heapq.nlargest(2, counts.items(), key=lambda kv: kv[1]))

heap = [(-count, word) for word, count in counts.items()]
heapq.heapify(heap)
print([heapq.heappop(heap) for _ in range(2)])
```

Negating the count turns the min-heap into a max-heap, so the most
frequent pops first; when counts tie, the tuple comparison falls through
to the word, giving alphabetical order for free. The `key=` form of
`nlargest` is clearer when it fits; the negated tuple is the form that
works inside a loop with pushes and pops.

Beware tuples whose second element cannot be compared, like a dictionary.
When two priorities tie Python compares the next field and fails. Put a
unique counter in the middle, as Module 4 did: `(priority, index, item)`.

## Merging sorted streams

Several sorted lists into one sorted list: put the head of each list in a
heap with its source, pop the smallest, and push the next item from that
source. Each item passes through a heap of size `k`, so merging `n` items
from `k` lists is n log k instead of sorting everything at n log n.

```python
import heapq

def merge_sorted(lists):
    heap = [(lst[0], i, 0) for i, lst in enumerate(lists) if lst]
    heapq.heapify(heap)
    out = []
    while heap:
        value, which, index = heapq.heappop(heap)
        out.append(value)
        if index + 1 < len(lists[which]):
            heapq.heappush(heap, (lists[which][index + 1], which, index + 1))
    return out

print(merge_sorted([[1, 4, 9], [2, 3, 10], [5, 6]]))
print(list(heapq.merge([1, 4, 9], [2, 3, 10], [5, 6])))
```

The tuple carries which list the value came from and where in it, so the
replacement can be found. `heapq.merge` is the library version. You built
this in the practice band as [merge k sorted](problem:p-merge-k-sorted).

## Two heaps for a running median

The median of everything seen so far, updated as values arrive. Keep the
smaller half in a max-heap (negated values) and the larger half in a
min-heap, balanced so their sizes differ by at most one. The median is at
the top of one or both.

```python
import heapq

class Median:
    def __init__(self):
        self.low = []
        self.high = []

    def add(self, x):
        heapq.heappush(self.low, -x)
        heapq.heappush(self.high, -heapq.heappop(self.low))
        if len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def median(self):
        if len(self.low) > len(self.high):
            return -self.low[0]
        return (-self.low[0] + self.high[0]) / 2

m = Median()
for x in [5, 15, 1, 3, 8]:
    m.add(x)
    print("after", x, "median is", m.median())
```

The `add` method pushes to `low`, moves the largest of `low` to `high`,
then rebalances if `high` got too big. Each step is log n, where sorting
after every arrival would be n log n each time. (The `class` here is the
same minimal use as for linked-list nodes: a bundle of two heaps with two
functions attached. `self` is the bundle.) This was
[median of a stream](problem:p-median-stream).

## When a heap is the answer

- "The k largest, smallest, closest, most frequent": heap of size k.
- "Repeatedly take the smallest and put something back": a heap, every
  time. Merging, scheduling, simulation, Dijkstra's shortest paths.
- "Smallest so far, over a stream": a heap or two.
- Need every item in order once: just sort. A heap gains nothing when you
  will pop everything anyway.

## Try it

:::problem a-kth-largest

:::problem a-k-closest

:::problem a-top-words

:::problem a-join-ropes

Next: [Greedy](../11-greedy).
