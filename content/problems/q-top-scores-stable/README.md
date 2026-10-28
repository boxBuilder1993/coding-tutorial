# Top scores, ties by arrival

`entries` is a list of `(name, score)` in the order people finished. Write
`top_k(entries, k)` that returns the names of the `k` highest scores, highest first;
when scores tie, whoever appears earlier in `entries` comes first. `k` is at most the
number of entries.

```static
top_k([("ana", 7), ("ben", 9), ("cy", 7), ("dee", 9)], 3)  ->  ["ben", "dee", "ana"]
```

The point is to practise relying on stability: sort by score only and let equal scores
keep their input order.

## Starter

```python
def top_k(entries, k):
    ...
```

## Hints

1. `sorted(entries, key=lambda e: -e[1])` keeps ties in input order because `sorted` is stable.
2. Do not use `reverse=True` with a positive key: it reverses the ties too.
3. Slice the first `k` and pull out the names.

## Approach

Negate the score in the key so bigger comes first without reversing the tie order. Slice and project to names.

## Reference

```python
def top_k(entries, k):
    return [name for name, score in sorted(entries, key=lambda e: -e[1])[:k]]
```
