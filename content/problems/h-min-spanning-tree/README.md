# Cheapest way to connect everything

`n` towns are numbered `0` to `n - 1` and `roads` lists possible `(a, b, cost)` links.
Write `min_connection_cost(n, roads)` that returns the smallest total cost of a set of
roads that connects every town, or `-1` if they cannot all be connected.

```static
min_connection_cost(4, [(0, 1, 1), (1, 2, 2), (2, 3, 3), (0, 3, 10), (1, 3, 4)])  ->  6
min_connection_cost(3, [(0, 1, 1)])  ->  -1
```

Kruskal's algorithm: sort roads by cost and take each one that joins two towns not already
connected. "Already connected" is answered by a **disjoint-set** (union-find): a `parent`
list where `find(x)` follows parents to a root, and `union(a, b)` links one root under the
other. Build it yourself; it is a dozen lines.

## Starter

```python
def min_connection_cost(n, roads):
    ...
```

## Hints

1. `parent = list(range(n))`. `find(x)`: while `parent[x] != x`, set `parent[x] = parent[parent[x]]` (shortcut) and move up. `union(a, b)`: find both roots; if equal return `False`, else link and return `True`.
2. Sort roads by cost; for each, if `union(a, b)` succeeds add its cost and count it. Done when `n - 1` roads are taken.
3. If fewer than `n - 1` roads were taken, return -1.

## Approach

Greedy on cost with a cycle check from union-find. Taking the cheapest safe edge each time is optimal. Sort dominates: E log E.

## Reference

```python
def min_connection_cost(n, roads):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    total = 0
    taken = 0
    for a, b, cost in sorted(roads, key=lambda r: r[2]):
        ra, rb = find(a), find(b)
        if ra == rb:
            continue
        parent[ra] = rb
        total += cost
        taken += 1
        if taken == n - 1:
            break
    return total if taken == n - 1 else -1
```
