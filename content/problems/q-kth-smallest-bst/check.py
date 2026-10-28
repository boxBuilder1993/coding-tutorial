from solution import kth_smallest
from checker import case, from_level_order as t

case("smallest", kth_smallest(t([3, 1, 4, None, 2]), 1), 1)
case("third", kth_smallest(t([5, 3, 6, 2, 4, None, None, 1]), 3), 3)
case("largest", kth_smallest(t([5, 3, 6, 2, 4, None, None, 1]), 6), 6)
case("single", kth_smallest(t([7]), 1), 7)
case("second", kth_smallest(t([3, 1, 4, None, 2]), 2), 2)
