from solution import in_both
from checker import case

case("two in common", in_both(["apple", "bread", "milk"], ["milk", "eggs", "apple"]), ["apple", "milk"])
case("nothing in common", in_both(["apple"], ["bread"]), [])
case("duplicates appear once", in_both(["a", "a", "b"], ["a", "a"]), ["a"])
case("result is sorted", in_both(["z", "y", "x"], ["x", "y", "z"]), ["x", "y", "z"])
