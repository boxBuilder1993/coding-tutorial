from solution import partition
from checker import case, from_list, to_list

case("classic", to_list(partition(from_list([1, 4, 3, 2, 5, 2]), 3)), [1, 2, 2, 4, 3, 5])
case("two nodes", to_list(partition(from_list([2, 1]), 2)), [1, 2])
case("empty", partition(None, 1), None)
case("all small", to_list(partition(from_list([1, 2]), 5)), [1, 2])
case("all large", to_list(partition(from_list([7, 8]), 5)), [7, 8])
case("terminates the list", to_list(partition(from_list([5, 1]), 3)), [1, 5])
