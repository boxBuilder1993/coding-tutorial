from solution import leaf_sum
from checker import case, from_level_order

case("example tree", leaf_sum(from_level_order([8, 3, 10, 1, 6, None, 14])), 21)
case("single node is a leaf", leaf_sum(from_level_order([5])), 5)
case("empty", leaf_sum(None), 0)
case("only one leaf deep down", leaf_sum(from_level_order([1, 2, None, 3])), 3)
case("full tree", leaf_sum(from_level_order([1, 2, 3, 4, 5, 6, 7])), 22)
