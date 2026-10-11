from solution import clean
from checker import case
case("messy", clean(["  Bread ", "", "MILK", "   "]), ["bread", "milk"])
case("empty", clean([]), [])
case("already clean", clean(["apple"]), ["apple"])
