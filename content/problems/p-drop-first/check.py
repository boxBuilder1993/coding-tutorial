from solution import rest
from checker import case
case("three", rest(["apple", "bread", "milk"]), ["bread", "milk"])
case("empty", rest([]), [])
case("one", rest([1]), [])
original = [1, 2]
rest(original)
case("original unchanged", original, [1, 2])
