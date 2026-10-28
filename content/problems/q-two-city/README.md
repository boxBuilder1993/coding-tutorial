# Cheapest way to send people to two cities

`costs` is a list of `(cost_a, cost_b)` for `2n` people: what it costs to send each to
city A or city B. Exactly `n` must go to each. Write `min_total(costs)` that returns the
smallest total cost.

```static
min_total([(10, 20), (30, 200), (400, 50), (30, 20)])  ->  110
min_total([(5, 1), (1, 5)])                            ->  2
```

The point is to practise a greedy on the **difference**: send everyone to A, then switch
the `n` people for whom switching to B saves the most.

## Starter

```python
def min_total(costs):
    ...
```

## Hints

1. Sort people by `cost_a - cost_b`. Those with the smallest difference (most negative) are the best to send to A.
2. First half of the sorted list goes to A, second half to B. Sum.

## Approach

Sorting by how much more A costs than B lets you pick the `n` people where A is relatively cheapest. n log n.

## Reference

```python
def min_total(costs):
    ordered = sorted(costs, key=lambda c: c[0] - c[1])
    n = len(costs) // 2
    return sum(c[0] for c in ordered[:n]) + sum(c[1] for c in ordered[n:])
```
