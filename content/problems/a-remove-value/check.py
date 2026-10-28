from solution import remove_all
from checker import case, from_list, to_list

case("scattered", to_list(remove_all(from_list([1, 2, 1, 3, 1]), 1)), [2, 3])
case("everything removed", remove_all(from_list([7, 7]), 7), None)
case("empty", remove_all(None, 7), None)
case("nothing matches", to_list(remove_all(from_list([1, 2]), 9)), [1, 2])
case("head removed", to_list(remove_all(from_list([5, 1, 2]), 5)), [1, 2])
case("tail removed", to_list(remove_all(from_list([1, 2, 5]), 5)), [1, 2])
case("consecutive matches", to_list(remove_all(from_list([1, 5, 5, 5, 2]), 5)), [1, 2])
