from solution import every_other
from checker import case
case("five", every_other(["a", "b", "c", "d", "e"]), ["a", "c", "e"])
case("empty", every_other([]), [])
case("two", every_other([1, 2]), [1])
