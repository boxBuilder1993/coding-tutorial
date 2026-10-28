from solution import max_path_sum
from checker import case, from_level_order as t

case("small", max_path_sum(t([1, 2, 3])), 6)
case("skip the root", max_path_sum(t([-10, 9, 20, None, None, 15, 7])), 42)
case("single negative", max_path_sum(t([-3])), -3)
case("all negative", max_path_sum(t([-2, -1, -3])), -1)
case("chain", max_path_sum(t([1, 2, None, 3, None, 4])), 10)
case("avoid negative branch", max_path_sum(t([5, -100, 4, None, None, 1, 2])), 11)
