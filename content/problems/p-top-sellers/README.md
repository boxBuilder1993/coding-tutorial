# Top sellers

`sales` is a list of item names, one per sale. Write `top_sellers(sales, k)`
that returns the `k` most sold items as `(item, count)` tuples, most sold
first. Items with the same count are ordered alphabetically. `k` may exceed
the number of distinct items.

```static
top_sellers(["milk", "bread", "milk", "apple", "bread", "milk"], 2)  ->  [("milk", 3), ("bread", 2)]
```

## Starter

```python
def top_sellers(sales, k):
    ...
```

## Hints

1. Count with a dictionary, then `sorted` with a `key` that sorts by count descending and name ascending.
2. `key=lambda p: (-p[1], p[0])` on the `items()`, then slice `[:k]`.

## Approach

Count, then sort the `(item, count)` pairs by `(-count, item)` so bigger counts come first and ties break alphabetically, then take the first `k`.

## Reference

```python
def top_sellers(sales, k):
    counts = {}
    for item in sales:
        counts[item] = counts.get(item, 0) + 1
    ranked = sorted(counts.items(), key=lambda p: (-p[1], p[0]))
    return ranked[:k]
```
