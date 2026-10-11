from solution import receipt_total
from checker import case
case("two lines", receipt_total("bread x 3 @ 25\nmilk x 2 @ 2.5"), 80.0, compare="approx")
case("empty", receipt_total(""), 0, compare="approx")
case("blank and padded lines", receipt_total("  bread x 1 @ 25  \n\n milk x 1 @ 2.5"), 27.5, compare="approx")
case("one line", receipt_total("eggs x 12 @ 0.5"), 6.0, compare="approx")
