---
title: Greedy algorithms in Python: when the obvious choice is the right one
description: Take the best local choice and never look back: interval scheduling, change-making, the jump game, and how to tell when greedy fails.
---
# Greedy

A **greedy** algorithm builds its answer one choice at a time, always
taking the choice that looks best right now, and never revisits a choice.
That sounds naive, and for many problems it is wrong. For a surprising
number it is exactly right, and when it is, it is usually the fastest
possible method: one pass, often after one sort.

The skill is not writing greedy code, which is easy. It is knowing when
greedy is correct.

## Making change

Give change for 67 using coins of 25, 10, 5 and 1 with the fewest coins.
Take the biggest coin that fits, repeat:

```python
def make_change(amount, coins):
    used = []
    for coin in sorted(coins, reverse=True):
        while amount >= coin:
            amount -= coin
            used.append(coin)
    return used

print(make_change(67, [25, 10, 5, 1]))
print(make_change(30, [25, 10, 1]))
```

The first answer is optimal. The second is not: 30 as `25 + 1 + 1 + 1 + 1 + 1`
is six coins, where `10 + 10 + 10` is three. Greedy fails here because
taking the 25 locked out the better path. With the usual coin systems
greedy happens to be right; with arbitrary coins it is not, and the
correct method is dynamic programming on the next page. Same code, right
for one input and wrong for another, which is why "it worked on my
example" is never enough for greedy.

## Scheduling the most meetings

Rooms, talks, deliveries: given intervals with a start and an end, pick as
many as possible that do not overlap. The greedy choice that works is
**always take the one that ends earliest** among those that do not clash
with what you already picked.

```python
def most_meetings(meetings):
    chosen = []
    last_end = float("-inf")
    for start, end in sorted(meetings, key=lambda m: m[1]):
        if start >= last_end:
            chosen.append((start, end))
            last_end = end
    return chosen

print(most_meetings([(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11)]))
```

Why earliest end? Finishing early leaves the most room for everything
after. The argument that makes this rigorous: whatever an optimal schedule
picks first, swapping it for the earliest-ending meeting cannot cause a
clash, so there is always an optimal schedule that starts with the greedy
choice; repeat. Picking the earliest **start** or the **shortest** meeting
both fail; try `[(1, 10), (2, 3), (4, 5)]` with shortest-first in your
head.

Sort then one pass: n log n. [Merge intervals](problem:p-merge-intervals)
in the practice band is the same sort followed by a different pass.

## The jump game

Each position in a list says how far you can jump forward from it. Can
you reach the end? Rather than exploring every path, track the furthest
position reachable so far:

```python
def can_reach_end(jumps):
    furthest = 0
    for i, jump in enumerate(jumps):
        if i > furthest:
            return False
        furthest = max(furthest, i + jump)
    return True

print(can_reach_end([2, 3, 1, 1, 4]))
print(can_reach_end([3, 2, 1, 0, 4]))
```

Linear, and correct because the only thing that matters about the past is
how far it lets you go. Many greedy solutions have this form: the state is
one number summarising everything so far.

## Pairing up

Children with appetites and biscuits with sizes; each child is content
with a biscuit at least as large as their appetite. How many can be
content? Sort both, and give the smallest biscuit that works to the
hungriest child it can satisfy, which is the same as walking both sorted
lists with two pointers:

```python
def content_children(appetites, biscuits):
    appetites.sort()
    biscuits.sort()
    child = 0
    for b in biscuits:
        if child < len(appetites) and b >= appetites[child]:
            child += 1
    return child

print(content_children([1, 2, 3], [1, 1]))
print(content_children([1, 2], [1, 2, 3]))
```

Each biscuit goes to the least demanding unserved child if it can; wasting
a large biscuit on a small appetite can only hurt. Assignment problems
where "smallest that fits" is obviously no worse than any alternative are
greedy, and two pointers over two sorted lists is the usual shape.

## Telling greedy from not

Greedy is right when the problem has two properties:

- **A choice that is safe to make without knowing the future.** Earliest
  end, furthest reach, smallest fit: a choice you can prove is part of
  some optimal answer.
- **What remains after the choice is the same problem, smaller.** After
  picking a meeting, the remaining problem is "schedule the meetings
  starting after it", with no memory of what was chosen.

The warning signs: the greedy choice needs a tie-break you cannot justify,
or a small counter-example like the `30` above exists. When in doubt, try
to break your greedy rule by hand on a five-item example before trusting
it. If it breaks, the problem probably needs the next page.

## Try it

:::problem a-most-meetings

:::problem a-fewest-coins-greedy

:::problem a-jump-game

:::problem a-content-children

Next: [Dynamic programming](../12-dynamic-programming).
