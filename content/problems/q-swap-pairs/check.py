from solution import swap_pairs
from checker import case, from_list, to_list

case("even", to_list(swap_pairs(from_list([1, 2, 3, 4]))), [2, 1, 4, 3])
case("odd", to_list(swap_pairs(from_list([1, 2, 3]))), [2, 1, 3])
case("empty", swap_pairs(None), None)
case("single", to_list(swap_pairs(from_list([1]))), [1])
head = from_list([1, 2])
new_head = swap_pairs(head)
case("relinks rather than copies", new_head.next is head, True)
