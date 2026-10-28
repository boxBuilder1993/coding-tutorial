from solution import right_view
from checker import case, from_level_order as t

case("classic", right_view(t([1, 2, 3, None, 5, None, 4])), [1, 3, 4])
case("left child only", right_view(t([1, 2])), [1, 2])
case("empty", right_view(None), [])
case("left deeper than right", right_view(t([1, 2, 3, 4])), [1, 3, 4])
case("full", right_view(t([1, 2, 3, 4, 5, 6, 7])), [1, 3, 7])
