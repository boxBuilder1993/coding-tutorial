from solution import remove_item
from checker import case

case("present", remove_item(["apple", "bread", "milk"], "bread"), ["apple", "milk"])
case("absent leaves it alone", remove_item(["apple", "milk"], "eggs"), ["apple", "milk"])
case("only the first occurrence goes", remove_item(["a", "b", "a"], "a"), ["b", "a"])
case("empty list", remove_item([], "apple"), [])
