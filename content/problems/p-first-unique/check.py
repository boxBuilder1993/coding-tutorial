from solution import first_unique
from checker import case
case("bread", first_unique(["milk", "bread", "milk", "eggs"]), "bread")
case("none unique", first_unique(["a", "a"]), None)
case("empty", first_unique([]), None)
case("first of several uniques", first_unique(["x", "y"]), "x")
