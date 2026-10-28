# Cheapest route with at most k stops

`flights` is a list of `(from, to, price)` one-way flights among cities numbered `0` to
`n - 1`. Write `cheapest(n, flights, src, dst, k)` that returns the cheapest price from
`src` to `dst` using at most `k` intermediate stops, or `-1` if impossible.

```static
cheapest(4, [(0, 1, 100), (1, 2, 100), (2, 0, 100), (1, 3, 600), (2, 3, 200)], 0, 3, 1)  ->  700
cheapest(3, [(0, 1, 100), (1, 2, 100), (0, 2, 500)], 0, 2, 1)  ->  200
cheapest(3, [(0, 1, 100), (1, 2, 100), (0, 2, 500)], 0, 2, 0)  ->  500
```

Dijkstra does not respect the stop limit. Instead relax every edge `k + 1` times from a
copy of the previous round's costs (Bellman-Ford, limited to `k + 1` rounds).

## Starter

```python
def cheapest(n, flights, src, dst, k):
    ...
```

## Hints

1. `cost = [inf] * n` with `cost[src] = 0`. Repeat `k + 1` times: `new = cost[:]`; for each flight, `new[to] = min(new[to], cost[frm] + price)`; then `cost = new`.
2. Copying each round means every path in round `r` uses exactly at most `r` flights.
3. Return `cost[dst]` or `-1`.

## Approach

Each round of edge relaxation extends paths by one flight; `k + 1` rounds allow `k` stops. Cost is rounds times flights.

## Reference

```python
def cheapest(n, flights, src, dst, k):
    INF = float("inf")
    cost = [INF] * n
    cost[src] = 0
    for _ in range(k + 1):
        new = cost[:]
        for frm, to, price in flights:
            if cost[frm] + price < new[to]:
                new[to] = cost[frm] + price
        cost = new
    return -1 if cost[dst] == INF else cost[dst]
```
