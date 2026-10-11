from solution import unique_count
from checker import case

case("with repeats", unique_count(["apple", "bread", "apple", "milk", "apple"]), 3)
case("empty", unique_count([]), 0)
case("no repeats", unique_count(["a", "b", "c"]), 3)
case("all the same", unique_count(["x", "x", "x"]), 1)
