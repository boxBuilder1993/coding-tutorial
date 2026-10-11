from solution import pair_sum
from checker import case
case("example", pair_sum([1, 3, 4, 6, 8], 10), (2, 3))
case("no pair", pair_sum([1, 2], 10), None)
case("ends", pair_sum([1, 5, 9], 10), (0, 2))
case("empty", pair_sum([], 1), None)
case("single", pair_sum([5], 10), None)
case("negatives", pair_sum([-4, -1, 2, 7], 1), (1, 2))
