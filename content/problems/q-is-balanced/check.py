from solution import is_balanced
from checker import case, from_level_order as t

case("balanced", is_balanced(t([3, 9, 20, None, None, 15, 7])), True)
case("unbalanced", is_balanced(t([1, 2, 2, 3, 3, None, None, 4, 4])), False)
case("empty", is_balanced(None), True)
case("single", is_balanced(t([1])), True)
case("chain of three", is_balanced(t([1, 2, None, 3])), False)
case("off by one is fine", is_balanced(t([1, 2, None])), True)
