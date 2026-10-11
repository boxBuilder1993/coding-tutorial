# Halve until under

A price is cut in half repeatedly until it is below `limit`. Write
`halvings(price, limit)` that returns how many halvings that takes. If the
price is already below the limit, return 0.

```static
halvings(100, 10)  ->  4     (100 -> 50 -> 25 -> 12.5 -> 6.25)
halvings(5, 10)    ->  0
```

## Starter

```python
def halvings(price, limit):
    ...
```

## Hints

1. Loop while `price >= limit`.
2. Inside: `price = price / 2` and count one more.

## Approach

The number of rounds depends on the values, which is why this is a `while`, not a `for`.

## Reference

```python
def halvings(price, limit):
    count = 0
    while price >= limit:
        price = price / 2
        count += 1
    return count
```
