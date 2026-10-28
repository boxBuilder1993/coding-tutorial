from solution import range_sums
from checker import case

case("three queries", range_sums([3, 1, 4, 1, 5], [(0, 2), (1, 3), (4, 4)]), [8, 6, 5])
case("no queries", range_sums([3, 1, 4, 1, 5], []), [])
case("whole list", range_sums([2, -3, 7], [(0, 2)]), [6])
case("single item ranges", range_sums([9, 8], [(0, 0), (1, 1)]), [9, 8])
n = 100000
items = [(i * 37) % 101 for i in range(n)]
queries = [((k * 7919) % n, ) for k in range(n)]
queries = [(min(a[0], (a[0] * 31 + 17) % n), max(a[0], (a[0] * 31 + 17) % n)) for a in queries]
prefix = [0]
for x in items:
    prefix.append(prefix[-1] + x)
expected = [prefix[j + 1] - prefix[i] for i, j in queries]
case("a hundred thousand queries", range_sums(items, queries), expected)
