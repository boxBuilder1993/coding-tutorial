from solution import min_depth
from checker import case, from_level_order

case("classic", min_depth(from_level_order([3, 9, 20, None, None, 15, 7])), 2)
case("one-child chain", min_depth(from_level_order([2, None, 3, None, 4])), 3)
case("empty", min_depth(None), 0)
case("single", min_depth(from_level_order([1])), 1)
case("left leaf shallow", min_depth(from_level_order([1, 2, 3, None, None, 4, 5])), 2)
