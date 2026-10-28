# Making change at the stand

Each drink costs 5. Customers pay with a 5, 10 or 20 note, in the order given in `bills`,
and you start with no money. Write `can_serve_all(bills)` that returns whether you can
give every customer correct change.

```static
can_serve_all([5, 5, 5, 10, 20])  ->  True
can_serve_all([5, 5, 10, 10, 20]) ->  False
can_serve_all([10])               ->  False
```

The point is to practise a greedy choice when breaking a 20: prefer giving a 10 and a 5
over three 5s, because 5s are more useful later.

## Starter

```python
def can_serve_all(bills):
    ...
```

## Hints

1. Count your fives and tens. A 5 adds a five. A 10 needs one five and adds a ten.
2. A 20 takes a ten and a five if possible, else three fives. If change cannot be made, return `False`.

## Approach

Keep counts of the two useful notes; for a 20 spend the 10 first since it has no other use. Linear.

## Reference

```python
def can_serve_all(bills):
    fives = tens = 0
    for b in bills:
        if b == 5:
            fives += 1
        elif b == 10:
            if fives == 0:
                return False
            fives -= 1
            tens += 1
        else:
            if tens > 0 and fives > 0:
                tens -= 1
                fives -= 1
            elif fives >= 3:
                fives -= 3
            else:
                return False
    return True
```
