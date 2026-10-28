from solution import pairs_with_difference
from checker import case

case("three pairs", pairs_with_difference([1, 5, 3, 4, 2], 2), 3)
case("repeats count once", pairs_with_difference([1, 1, 3], 2), 1)
case("no pairs", pairs_with_difference([1, 2, 3], 5), 0)
case("empty", pairs_with_difference([], 1), 0)
case("negative values", pairs_with_difference([-2, 0, 2, 4], 2), 3)
big = list(range(0, 300000, 3))
case("a hundred thousand values", pairs_with_difference(big, 3), 99999)
case("a hundred thousand values, no pairs", pairs_with_difference(big, 1), 0)
