from solution import same_items
from checker import case
case("same with repeats", same_items(["apple", "milk", "apple"], ["milk", "apple"]), True)
case("different", same_items(["apple"], ["apple", "milk"]), False)
case("both empty", same_items([], []), True)
