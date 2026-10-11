# How many of this item?

Write `how_many(basket, item)` that returns how many times `item` appears
in the list `basket`.

```static
how_many(["apple", "bread", "apple"], "apple")  ->  2
how_many(["apple"], "milk")                     ->  0
```

## Starter

```python
def how_many(basket, item):
    ...
```

## Hints

1. Lists have a method for this.
2. `basket.count(item)`

## Approach

`count` does the loop for you.

## Reference

```python
def how_many(basket, item):
    return basket.count(item)
```
