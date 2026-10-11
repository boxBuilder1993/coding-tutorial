from solution import two_sum
from checker import case
case("example", two_sum([2, 7, 11, 15], 9), (0, 1))
case("no pair", two_sum([1, 2], 10), None)
case("pair at the end", two_sum([3, 2, 4], 6), (1, 2))
case("same value twice", two_sum([3, 3], 6), (0, 1))
case("does not reuse one element", two_sum([3], 6), None)
case("negatives", two_sum([-1, -2, -3, -4], -6), (1, 3))
