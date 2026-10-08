# Swap two names

`first` refers to `"apple"` and `second` refers to `"bread"`. Make them swap,
so that `first` refers to `"bread"` and `second` to `"apple"`, then print both
on one line, `first` then `second`.

```static
bread apple
```

Do this using only the names. Do not write `"bread"` or `"apple"` again.

## Starter

```python
first = "apple"
second = "bread"
# swap them

print(first, second)
```

## Hints

1. If you write `first = second` straight away, the old value of `first` is lost. Keep it somewhere first.
2. Use a third name: `temp = first`, then `first = second`, then `second = temp`.

## Approach

Three assignments through a temporary name. Python also allows
`first, second = second, first` on one line, which you will meet later.

## Reference

```python
first = "apple"
second = "bread"
temp = first
first = second
second = temp
print(first, second)
```
