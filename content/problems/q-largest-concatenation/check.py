from solution import largest_number
from checker import case

case("two pieces", largest_number([10, 2]), "210")
case("classic", largest_number([3, 30, 34, 5, 9]), "9534330")
case("all zeros", largest_number([0, 0]), "0")
case("single", largest_number([1]), "1")
case("tricky prefix", largest_number([121, 12]), "12121")
case("another prefix", largest_number([432, 43243]), "43243432")
