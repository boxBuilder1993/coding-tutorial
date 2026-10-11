from solution import add_item
from checker import case

case("append to one", add_item(["apple"], "bread"), ["apple", "bread"])
case("append to empty", add_item([], "milk"), ["milk"])
case("returns the list, not None", add_item(["a"], "b") is not None, True)
original = ["apple"]
add_item(original, "bread")
case("changes the original list in place", original, ["apple", "bread"])
