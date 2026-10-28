# Where to start the loop

Driving a circular route, station `i` provides `gas[i]` fuel and it costs `cost[i]` to
reach the next station. Starting with an empty tank at some station, write
`start_station(gas, cost)` that returns the index you must start from to complete the
loop, or `-1` if impossible. If a solution exists it is unique.

```static
start_station([1, 2, 3, 4, 5], [3, 4, 5, 1, 2])  ->  3
start_station([2, 3, 4], [3, 4, 3])              ->  -1
```

The point is to practise a one-pass greedy: when the tank goes negative, nothing before
this point can be the start.

## Starter

```python
def start_station(gas, cost):
    ...
```

## Hints

1. If total gas is less than total cost, return -1. Otherwise a start exists.
2. Walk once with a running tank and a candidate start. When the tank drops below zero, set the candidate to the next station and reset the tank to zero.

## Approach

A negative tank at station `i` rules out every start between the candidate and `i`. Resetting the candidate once per failure gives a linear pass; the total check guarantees the final candidate works.

## Reference

```python
def start_station(gas, cost):
    if sum(gas) < sum(cost):
        return -1
    tank = 0
    start = 0
    for i in range(len(gas)):
        tank += gas[i] - cost[i]
        if tank < 0:
            start = i + 1
            tank = 0
    return start
```
