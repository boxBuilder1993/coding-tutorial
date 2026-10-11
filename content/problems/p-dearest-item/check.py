from solution import dearest
from checker import case
case("three", dearest([("milk", 2.5), ("apple", 40), ("bread", 25)]), "apple")
case("one", dearest([("x", 1)]), "x")
case("not alphabetical", dearest([("zz", 1), ("aa", 2)]), "aa")
