from solution import pairs_with_sum
from checker import case

case("with repeats", pairs_with_sum([1, 1, 2, 3, 3, 4, 5], 6), [[1, 5], [2, 4], [3, 3]])
case("none", pairs_with_sum([1, 2], 10), [])
case("empty", pairs_with_sum([], 1), [])
case("same value twice needs two copies", pairs_with_sum([3], 6), [])
case("many copies", pairs_with_sum([2, 2, 2, 2], 4), [[2, 2]])
case("negatives", pairs_with_sum([-3, -1, 0, 1, 3], 0), [[-3, 3], [-1, 1]])
