from solution import by_frequency
from checker import case

case("example", by_frequency([4, 1, 2, 2, 3, 3, 3]), [3, 3, 3, 2, 2, 1, 4])
case("empty", by_frequency([]), [])
case("all unique", by_frequency([3, 1, 2]), [1, 2, 3])
case("all same", by_frequency([5, 5]), [5, 5])
case("ties by value", by_frequency([2, 1, 2, 1]), [1, 1, 2, 2])
case("strings", by_frequency(["b", "a", "b", "c"]), ["b", "b", "a", "c"])
