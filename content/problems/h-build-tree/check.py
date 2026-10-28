from solution import build
from checker import case, to_level_order

case("classic", to_level_order(build([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])), [3, 9, 20, None, None, 15, 7])
case("empty", build([], []), None)
case("single", to_level_order(build([1], [1])), [1])
case("left chain", to_level_order(build([1, 2, 3], [3, 2, 1])), [1, 2, None, 3])
case("right chain", to_level_order(build([1, 2, 3], [1, 2, 3])), [1, None, 2, None, 3])
case("full", to_level_order(build([1, 2, 4, 5, 3, 6, 7], [4, 2, 5, 1, 6, 3, 7])), [1, 2, 3, 4, 5, 6, 7])
