# Tuples and sets

Two more structures. Each does one job that lists and dicts do badly.

## Tuples: values that belong together

A **tuple** is a fixed group of values, written with parentheses. Use it when
a few values form one thing, like an item and its price, or a position as
`(row, column)`.

```python
pair = ("bread", 25)
print(pair[0])
print(pair[1])
print(len(pair))
```

Indexing and slicing work as for lists, but a tuple **cannot be changed**: no
`append`, no assigning to a position. That is the point. A tuple says "these
go together and this is the complete set".

## Unpacking

A tuple's values can be pulled out into separate names in one line.

```python
pair = ("bread", 25)
item, price = pair
print(item)
print(price)
```

This is also how a function returns two things, and it is the one-line swap
promised back in the Names page:

```python
def cheapest_and_dearest(prices):
    return min(prices), max(prices)

low, high = cheapest_and_dearest([40, 25, 2.5])
print(low, high)

a, b = "apple", "bread"
a, b = b, a
print(a, b)
```

The parentheses are optional when writing a tuple; the commas make it one.

## Sets: no duplicates, fast membership

A **set** holds values with no order and no repeats. Build one with curly
braces, or from a list with `set()`.

```python
basket = ["apple", "bread", "apple", "milk", "apple"]
unique = set(basket)
print(unique)
print(len(unique))
```

Adding a value already present does nothing. `in` is fast however big the set
grows, which is why sets are the answer to "have I seen this before?".

```python
seen = set()
seen.add("apple")
seen.add("bread")
seen.add("apple")
print(seen)
print("apple" in seen)
print("milk" in seen)
```

Sets have no positions, so `seen[0]` is an error. To get an empty set write
`set()`; `{}` is an empty dictionary.

## Combining sets

```python
shop_a = {"apple", "bread", "milk"}
shop_b = {"bread", "milk", "eggs"}
print(shop_a & shop_b)
print(shop_a | shop_b)
print(shop_a - shop_b)
```

`&` is what both have, `|` is everything in either, `-` is what the first has
that the second does not.

## Which structure?

| You need | Use |
|----------|-----|
| An ordered collection you will add to and change | list |
| A few values that form one thing, never changed | tuple |
| Lookup by a key you choose | dict |
| Uniqueness or fast "is it in there?" | set |

## Try it

:::problem split-pair

:::problem unique-items

:::problem in-both

Next: [Built-in functions](../07-built-in-functions).
