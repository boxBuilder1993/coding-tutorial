from solution import middle
from checker import case, from_list, to_list

case("odd length", to_list(middle(from_list([1, 2, 3, 4, 5]))), [3, 4, 5])
case("even length, second middle", to_list(middle(from_list([1, 2, 3, 4]))), [3, 4])
case("single", to_list(middle(from_list([9]))), [9])
case("two nodes", to_list(middle(from_list([1, 2]))), [2])
head = from_list([1, 2, 3])
case("returns the existing node", middle(head) is head.next, True)
