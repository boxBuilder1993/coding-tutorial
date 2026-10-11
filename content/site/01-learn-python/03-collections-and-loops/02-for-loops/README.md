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

`range` produces a run of numbers to loop over. With one argument it starts
at 0 and stops **before** that number, so `range(3)` gives 0, 1, 2.

```python
for i in range(3):
    print(i)
```

With two arguments, the first is where to start. `range(1, 4)` gives 1, 2, 3:
it starts at 1 and still stops before 4. The same half-open rule as slicing.

```python
for i in range(1, 4):
    print("Box", i)

for year in range(2020, 2024):
    print(year)
```

A third argument is the step. `range(0, 20, 5)` gives 0, 5, 10, 15. A negative
step counts down, and then the start must be the larger number.

```python
for i in range(0, 20, 5):
    print(i)

for i in range(3, 0, -1):
    print(i)
print("Go!")
```

Old tutorials and Python 2 code use `xrange`. It no longer exists; `range`
does the same job. Run this to see the error you would get:

```python
for i in xrange(3):
    print(i)
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
