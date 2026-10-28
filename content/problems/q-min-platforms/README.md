# Platforms needed

`arrivals` and `departures` list, for each train, when it arrives and when it leaves; a
platform freed at time `t` cannot be reused by a train arriving at `t`. Write
`min_platforms(arrivals, departures)` that returns the fewest platforms so no train waits.

```static
min_platforms([900, 940, 950, 1100, 1500, 1800], [910, 1200, 1120, 1130, 1900, 2000])  ->  3
min_platforms([100], [200])  ->  1
```

The point is to practise the "sort events and sweep" technique: the answer is the
maximum number of trains present at once.

## Starter

```python
def min_platforms(arrivals, departures):
    ...
```

## Hints

1. Sort both lists separately. Walk them with two indices: an arrival before (or at) the next departure adds a train; otherwise a departure removes one.
2. Track the running count's maximum.

## Approach

Two sorted lists and two pointers: process whichever event comes first, counting trains present. The peak is the answer. n log n.

## Reference

```python
def min_platforms(arrivals, departures):
    arr = sorted(arrivals)
    dep = sorted(departures)
    i = j = 0
    current = best = 0
    while i < len(arr):
        if arr[i] <= dep[j]:
            current += 1
            best = max(best, current)
            i += 1
        else:
            current -= 1
            j += 1
    return best
```
