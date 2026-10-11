# For loops

A `for` loop runs a block once for each item in a list. The name after `for`
takes each value in turn.

```python
items = ["apple", "bread", "milk"]
for item in items:
    print("Buying", item)
```

Three iterations, one per item. The indented block is the loop body; code
after it, unindented, runs once the loop is finished.

## Accumulating a result

The most common loop shape: start with an empty result, add to it each time
round, use it at the end.

```python
prices = [40, 25, 2.5]
total = 0
for price in prices:
    total += price
print("Total:", total)
```

`total` must be created before the loop. Inside, `total += price` updates it.
The same shape counts things, builds strings, or finds the biggest value:

```python
prices = [40, 25, 60, 2.5]
biggest = prices[0]
for price in prices:
    if price > biggest:
        biggest = price
print(biggest)
```

## Looping over numbers

`range(n)` produces the numbers from 0 up to but not including `n`.
`range(a, b)` goes from `a` to `b - 1`.

```python
for i in range(3):
    print(i)

for i in range(1, 4):
    print("Box", i)
```

## Looping over the characters of a string

A string is a sequence too, so `for` walks through its characters.

```python
for ch in "bread":
    print(ch)
```

And `split`, from the string methods page, turns a sentence into a list of
words you can loop over:

```python
line = "apple bread milk"
for word in line.split():
    print(word.upper())
```

## Try it

:::problem total-price

:::problem count-expensive

:::problem longest-name

Next: [More list operations](../03-more-list-operations).
