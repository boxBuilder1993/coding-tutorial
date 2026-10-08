from solution import reverse_list
from checker import case, from_list, to_list

case("five nodes", to_list(reverse_list(from_list([1, 2, 3, 4, 5]))), [5, 4, 3, 2, 1])
case("empty list", reverse_list(None), None)
case("single node", to_list(reverse_list(from_list([7]))), [7])
case("two nodes", to_list(reverse_list(from_list([1, 2]))), [2, 1])
