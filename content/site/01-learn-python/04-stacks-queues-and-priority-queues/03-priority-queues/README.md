---
title: Priority queues in Python with heapq
description: Always take the smallest: heappush, heappop, tuples for priorities, heapify, nsmallest and nlargest.
---
# Priority queues

Sometimes the order things come out is neither "most recent" nor "oldest"
but "most important". A **priority queue** always gives you the smallest
value it holds, whatever order the values went in. Urgent orders first,
cheapest option first, nearest deadline first.

You could keep a list and call `min` each time, but `min` looks at every
item, and removing it shifts the rest. The standard library's `heapq` module
keeps a list arranged so that the smallest item is always at position 0 and
both adding and removing are fast.

```python
import heapq

prices = []
heapq.heappush(prices, 40)
heapq.heappush(prices, 2.5)
heapq.heappush(prices, 25)
print(prices[0])

print(heapq.heappop(prices))
print(heapq.heappop(prices))
print(heapq.heappop(prices))
```

`heappush` adds a value. `heappop` removes and returns the smallest.
`prices[0]` peeks at the smallest without removing it. Do not use `append`
or `sort` on a list you are treating as a heap; only the `heapq` functions
keep it arranged correctly.

If you print the list between pushes you will see it is not sorted. It has a
special arrangement called a **heap** that only promises the smallest is
first. That is enough.

## Priorities with data attached

To attach information to a priority, push tuples. Python compares tuples
one position at a time: the first values decide, and only if they are equal
does it look at the second values, then the third. So `(priority, item)` is
ordered by priority. Smaller numbers come out first; if you want "higher
priority first", use negative numbers.

```python
import heapq

orders = []
heapq.heappush(orders, (3, "bread"))
heapq.heappush(orders, (1, "wedding cake"))
heapq.heappush(orders, (2, "sandwiches"))

while orders:
    priority, item = heapq.heappop(orders)
    print(priority, item)
```

If two priorities tie, Python compares the second values, so the items must
be comparable with each other. Strings and numbers are fine. When they are
not, or when you want ties to come out in arrival order, push
`(priority, count, item)` where `count` goes up by one with every push:
the count breaks the tie and the item is never compared.

```python
import heapq

orders = []
count = 0
for priority, item in [(1, "cake"), (1, "rolls"), (0, "bread")]:
    heapq.heappush(orders, (priority, count, item))
    count += 1

while orders:
    priority, count, item = heapq.heappop(orders)
    print(priority, item)
```

## Starting from a list

`heapify` turns an existing list into a heap in place. `nsmallest` and
`nlargest` give the k smallest or largest without emptying it.

```python
import heapq

prices = [40, 25, 2.5, 60, 15]
heapq.heapify(prices)
print(prices)
print(prices[0])

print(heapq.nsmallest(2, prices))
print(heapq.nlargest(2, prices))
```

The second line of output shows that `heapify` rearranged the list: it is
in heap order now, not the order you wrote. If you need the original order
kept, heapify a copy.

## Which one?

| Comes out first | Structure | Operations |
|-----------------|-----------|------------|
| Most recently added | stack: a list | `append`, `pop` |
| Oldest | queue: a `deque` | `append`, `popleft` |
| Smallest | priority queue: `heapq` on a list | `heappush`, `heappop` |

## Try it

:::problem next-urgent

:::problem cheapest-k

:::problem process-by-priority

Next: [Practice](../../05-practice).
