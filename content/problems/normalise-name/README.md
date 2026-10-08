# Normalise an item name

Item names typed by staff are messy: extra spaces at the ends, random
capitals. Write `normalise(name)` that returns the name with the spaces at
both ends removed and everything in lowercase.

```static
normalise("  Sourdough Bread ")  ->  "sourdough bread"
normalise("MILK")                ->  "milk"
```

## Starter

```python
def normalise(name):
    ...
```

## Hints

1. `strip` removes spaces at the ends, `lower` handles capitals.
2. Methods can be chained: `name.strip().lower()`.

## Approach

Each method returns a new string, so the second call works on the result of the first.

## Reference

```python
def normalise(name):
    return name.strip().lower()
```
