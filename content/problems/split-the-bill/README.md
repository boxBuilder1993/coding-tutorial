# Split the bill

A bill of 100 is split equally among 4 people. Then, separately, 20 eggs are
packed into boxes of 6.

Print three lines: each person's share, how many full boxes you can pack, and
how many eggs are left over.

```static
25.0
3
2
```

## Starter

```python
print(100 / 4)
print(...)
print(...)
```

## Hints

1. `//` divides and drops the remainder. `%` gives only the remainder.
2. `20 // 6` is 3 and `20 % 6` is 2.

## Approach

Plain division with `/` gives `25.0`. Whole boxes are `20 // 6`, leftovers are `20 % 6`.

## Reference

```python
print(100 / 4)
print(20 // 6)
print(20 % 6)
```
