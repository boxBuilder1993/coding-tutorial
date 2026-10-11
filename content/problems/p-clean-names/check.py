from solution import clean
from checker import case
case("messy", clean(["  Bread ", "", "MILK", "   "]), ["bread", "milk"])
case("empty", clean([]), [])
case("already clean", clean(["apple"]), ["apple"])
case("inner spaces are kept", clean(["  Ice Cream "]), ["ice cream"])
case("order kept", clean(["c", " b", "a "]), ["c", "b", "a"])
