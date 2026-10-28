from solution import smaller_to_right
from checker import case
import bisect

case("classic", smaller_to_right([5, 2, 6, 1]), [2, 1, 1, 0])
case("equal values", smaller_to_right([-1, -1]), [0, 0])
case("empty", smaller_to_right([]), [])
case("descending", smaller_to_right([4, 3, 2, 1]), [3, 2, 1, 0])
case("ascending", smaller_to_right([1, 2, 3]), [0, 0, 0])
n = 40000
big = [(i * 7919) % 10007 for i in range(n)]
expected = []
seen = []
for v in reversed(big):
    expected.append(bisect.bisect_left(seen, v))
    bisect.insort(seen, v)
expected.reverse()
case("forty thousand", smaller_to_right(big), expected)
