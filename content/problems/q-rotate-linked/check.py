from solution import rotate_right
from checker import case, from_list, to_list

case("by two", to_list(rotate_right(from_list([1, 2, 3, 4, 5]), 2)), [4, 5, 1, 2, 3])
case("wraps", to_list(rotate_right(from_list([1, 2]), 3)), [2, 1])
case("empty", rotate_right(None, 4), None)
case("by zero", to_list(rotate_right(from_list([1, 2, 3]), 0)), [1, 2, 3])
case("full turn", to_list(rotate_right(from_list([1, 2, 3]), 3)), [1, 2, 3])
case("single", to_list(rotate_right(from_list([9]), 5)), [9])
