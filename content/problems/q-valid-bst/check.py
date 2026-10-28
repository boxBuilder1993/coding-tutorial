from solution import is_bst
from checker import case, from_level_order as t

case("small valid", is_bst(t([2, 1, 3])), True)
case("deep violation", is_bst(t([5, 1, 4, None, None, 3, 6])), False)
case("empty", is_bst(None), True)
case("ancestor violation", is_bst(t([10, 5, 15, None, None, 6, 20])), False)
case("duplicates not allowed", is_bst(t([2, 2])), False)
case("larger valid", is_bst(t([8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13])), True)
