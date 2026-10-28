from solution import height
from checker import case, from_level_order

case("example tree", height(from_level_order([8, 3, 10, 1, 6, None, 14])), 3)
case("single node", height(from_level_order([1])), 1)
case("empty", height(None), 0)
case("left chain", height(from_level_order([1, 2, None, 3, None, 4])), 4)
case("two levels", height(from_level_order([1, 2, 3])), 2)
