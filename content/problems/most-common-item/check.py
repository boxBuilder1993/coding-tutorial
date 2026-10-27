from solution import most_common_item
from checker import case

case("clear winner", most_common_item(["apple", "bread", "apple"]), "apple")
case("tie goes to the first seen", most_common_item(["milk", "bread", "bread", "milk"]), "milk")
case("single item", most_common_item(["eggs"]), "eggs")
case("numbers", most_common_item([3, 1, 3, 2, 1, 3]), 3)
case("winner appears late", most_common_item(["a", "b", "c", "c", "c"]), "c")
