from solution import has_path_sum
from checker import case, from_level_order as t

case("classic", has_path_sum(t([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]), 22), True)
case("no such path", has_path_sum(t([1, 2, 3]), 5), False)
case("empty", has_path_sum(None, 0), False)
case("single node match", has_path_sum(t([7]), 7), True)
case("not a leaf", has_path_sum(t([1, 2]), 1), False)
case("negatives", has_path_sum(t([1, -2, 3]), -1), True)
