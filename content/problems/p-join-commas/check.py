from solution import listing
from checker import case
case("three", listing(["apple", "bread", "milk"]), "apple, bread, milk")
case("empty", listing([]), "")
case("one", listing(["milk"]), "milk")
