from solution import longest_ones
from checker import case

case("classic", longest_ones([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2), 6)
case("no flips, all zero", longest_ones([0, 0, 0], 0), 0)
case("more flips than zeros", longest_ones([0, 0], 5), 2)
case("all ones", longest_ones([1, 1, 1], 0), 3)
case("empty", longest_ones([], 1), 0)
case("one flip", longest_ones([1, 0, 1, 1, 0, 1], 1), 4)
