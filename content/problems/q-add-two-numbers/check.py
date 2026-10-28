from solution import add
from checker import case, from_list, to_list

case("342 + 465", to_list(add(from_list([2, 4, 3]), from_list([5, 6, 4]))), [7, 0, 8])
case("99 + 1", to_list(add(from_list([9, 9]), from_list([1]))), [0, 0, 1])
case("0 + 0", to_list(add(from_list([0]), from_list([0]))), [0])
case("different lengths", to_list(add(from_list([1]), from_list([9, 9, 9]))), [0, 0, 0, 1])
case("one empty", to_list(add(None, from_list([5]))), [5])
