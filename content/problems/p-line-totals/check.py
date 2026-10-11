from solution import line_totals
from checker import case
case("two lines", line_totals([("bread", 3, 25), ("milk", 2, 2.5)]), [75, 5.0])
case("empty", line_totals([]), [])
case("quantity zero", line_totals([("x", 0, 9)]), [0])
