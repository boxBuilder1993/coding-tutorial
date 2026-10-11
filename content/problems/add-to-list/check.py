from solution import add_item
from checker import case

case("append to one", add_item(["apple"], "bread"), ["apple", "bread"])
case("append to empty", add_item([], "milk"), ["milk"])
original = ["apple"]
add_item(original, "bread")
case("changes the original list in place", original, ["apple", "bread"])
