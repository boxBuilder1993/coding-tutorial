from solution import steps_to_find
from checker import case

case("last item", steps_to_find([3, 5, 7], 7), 3)
case("first item", steps_to_find([3, 5, 7], 3), 1)
case("absent", steps_to_find([3, 5, 7], 9), 3)
case("empty list", steps_to_find([], 9), 0)
case("stops at the first match", steps_to_find([1, 2, 2, 2], 2), 2)
case("a thousand items, absent", steps_to_find(list(range(1000)), -1), 1000)
