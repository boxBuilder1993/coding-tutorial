from solution import has_duplicate
from checker import case

case("one repeat", has_duplicate([1, 2, 3, 2]), True)
case("all different", has_duplicate([1, 2, 3]), False)
case("empty", has_duplicate([]), False)
case("single item", has_duplicate([7]), False)
case("strings", has_duplicate(["apple", "bread", "apple"]), True)
case("repeat at the ends", has_duplicate([5, 1, 2, 3, 5]), True)
big = list(range(60000))
case("sixty thousand, all different", has_duplicate(big), False)
case("sixty thousand, last repeats the first", has_duplicate(big + [0]), True)
