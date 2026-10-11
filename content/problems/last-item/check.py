from solution import last_item
from checker import case

case("three strings", last_item(["apple", "bread", "milk"]), "milk")
case("single item", last_item([7]), 7)
case("numbers", last_item([1, 2, 3, 4, 5]), 5)
