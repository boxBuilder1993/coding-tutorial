# Update stock

The shop starts the day with 10 loaves of bread. It sells 3. Starting from the
code below, reduce `stock` by 3 without typing `7` anywhere, then print it.

```static
7
```

## Starter

```python
stock = 10
# sell three loaves
print(stock)
```

## Hints

1. A name can be updated using its own current value: `stock = stock - 3`.
2. `stock -= 3` is the short form of the same thing.

## Approach

Assign the new value computed from the old: `stock = stock - 3` or `stock -= 3`, then print.

## Reference

```python
stock = 10
stock -= 3
print(stock)
```
