from solution import pair_count
from checker import case

case("four items", pair_count(4), 6)
case("one item", pair_count(1), 0)
case("no items", pair_count(0), 0)
case("a hundred items", pair_count(100), 4950)
case("a thousand items", pair_count(1000), 499500)
case("returns an int", type(pair_count(10)), int)
