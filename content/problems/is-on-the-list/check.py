from solution import on_list
from checker import case

case("present", on_list(["apple", "bread"], "bread"), True)
case("absent", on_list(["apple", "bread"], "milk"), False)
case("empty list", on_list([], "apple"), False)
case("whole value must match", on_list(["apple pie"], "apple"), False)
