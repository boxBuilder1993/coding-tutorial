from solution import three_sum
from checker import case
from collections import Counter


def same(actual, expected):
    return sorted(tuple(t) for t in actual) == sorted(tuple(t) for t in expected)


case("classic", three_sum([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]], compare=same)
case("zeros", three_sum([0, 0, 0, 0]), [[0, 0, 0]], compare=same)
case("too short", three_sum([1, 2]), [], compare=same)
case("none", three_sum([1, 2, 3]), [], compare=same)
case("mixed", three_sum([-2, -1, 1, 1, 3]), [[-2, -1, 3], [-2, 1, 1]], compare=same)
big = [(i * 7919) % 401 - 200 for i in range(1500)]
cnt = Counter(big)
distinct = sorted(cnt)
expected = set()
for a in distinct:
    for b in distinct:
        if b < a:
            continue
        c = -a - b
        if c < b or c not in cnt:
            continue
        if all(cnt[v] >= k for v, k in Counter([a, b, c]).items()):
            expected.add((a, b, c))
case("fifteen hundred values", three_sum(big), [list(t) for t in expected], compare=same)
