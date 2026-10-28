from solution import closest
from checker import case

case("tie goes to smaller", closest([1, 4, 6, 9], 5), 4)
case("closer above", closest([1, 4, 6, 9], 7), 6)
case("beyond the end", closest([1, 4, 6, 9], 100), 9)
case("before the start", closest([1, 4, 6, 9], -3), 1)
case("exact", closest([1, 4, 6, 9], 6), 6)
case("single", closest([5], 1), 5)
big = list(range(0, 2 * 10 ** 6, 2))
case("a million items", [closest(big, t) for t in (1, 999999, 1000000, 3 * 10 ** 6)], [0, 999998, 1000000, 1999998])
