from solution import all_in_stock
from checker import case

case("all positive", all_in_stock([3, 1, 5]), True)
case("one zero", all_in_stock([3, 0, 5]), False)
case("negative", all_in_stock([2, -1]), False)
case("empty", all_in_stock([]), True)
case("single zero", all_in_stock([0]), False)
case("returns a bool", type(all_in_stock([1])), bool)
