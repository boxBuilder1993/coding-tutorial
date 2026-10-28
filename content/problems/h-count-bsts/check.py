from solution import count_trees
from checker import case

case("one", count_trees(1), 1)
case("three", count_trees(3), 5)
case("zero", count_trees(0), 1)
case("four", count_trees(4), 14)
case("ten", count_trees(10), 16796)
case("nineteen", count_trees(19), 1767263190)
