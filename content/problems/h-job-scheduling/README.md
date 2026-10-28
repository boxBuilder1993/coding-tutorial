# Most profitable non-overlapping jobs

`jobs` is a list of `(start, end, profit)`. Two jobs may both be taken if one ends no later
than the other starts. Write `max_profit(jobs)` that returns the largest total profit from
a set of compatible jobs.

```static
max_profit([(1, 3, 50), (2, 4, 10), (3, 5, 40), (3, 6, 70)])  ->  120     (1-3 and 3-6)
max_profit([(1, 2, 5)])  ->  5
```

Sort by end. `best[i]` is the best profit using the first `i` jobs; for job `i`, either skip
it or take it plus `best` of the last job ending at or before its start, found with
`bisect`.

## Starter

```python
def max_profit(jobs):
    ...
```

## Hints

1. Sort by end time. Keep a list `ends` of end times for `bisect_right(ends, start)`, which gives how many earlier jobs are compatible.
2. `best[i + 1] = max(best[i], best[k] + profit)` where `k` is that count.

## Approach

Weighted interval scheduling: DP over jobs in end order with a binary search for the predecessor. n log n.

## Reference

```python
import bisect

def max_profit(jobs):
    jobs = sorted(jobs, key=lambda j: j[1])
    ends = [j[1] for j in jobs]
    best = [0]
    for i, (start, end, profit) in enumerate(jobs):
        k = bisect.bisect_right(ends, start, 0, i)
        best.append(max(best[-1], best[k] + profit))
    return best[-1]
```
