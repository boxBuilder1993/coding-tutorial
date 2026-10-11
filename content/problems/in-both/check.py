from solution import in_both
from checker import case

case("two in common", in_both(["apple", "bread", "milk"], ["milk", "eggs", "apple"]), ["apple", "milk"], compare="sorted")
case("nothing in common", in_both(["apple"], ["bread"]), [], compare="sorted")
case("duplicates appear once", in_both(["a", "a", "b"], ["a", "a"]), ["a"], compare="sorted")
case("returns a list", type(in_both(["x"], ["x"])).__name__, "list")
