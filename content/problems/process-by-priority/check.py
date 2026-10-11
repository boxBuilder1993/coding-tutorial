from solution import in_priority_order
from checker import case

case("three orders", in_priority_order([(3, "bread"), (1, "wedding cake"), (2, "sandwiches")]), ["wedding cake", "sandwiches", "bread"])
case("empty", in_priority_order([]), [])
case("already in order", in_priority_order([(1, "a"), (2, "b")]), ["a", "b"])
case("many", in_priority_order([(i, str(i)) for i in range(9, -1, -1)]), [str(i) for i in range(10)])
