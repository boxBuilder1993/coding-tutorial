from solution import same
from checker import case, from_level_order as t

case("identical", same(t([1, 2, 3]), t([1, 2, 3])), True)
case("different shape", same(t([1, 2]), t([1, None, 2])), False)
case("both empty", same(None, None), True)
case("one empty", same(t([1]), None), False)
case("different value", same(t([1, 2, 3]), t([1, 2, 4])), False)
case("deep match", same(t([5, 3, 8, 1, 4, 7, 9]), t([5, 3, 8, 1, 4, 7, 9])), True)
