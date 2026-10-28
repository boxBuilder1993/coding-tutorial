from solution import merge_three
from checker import case

case("interleaved", merge_three([1, 4], [2, 3], [0, 5]), [0, 1, 2, 3, 4, 5])
case("two empty", merge_three([], [], [7]), [7])
case("all empty", merge_three([], [], []), [])
case("repeats", merge_three([1, 1], [1], [1, 2]), [1, 1, 1, 1, 2])
case("one list after the others", merge_three([1, 2], [3, 4], [5, 6]), [1, 2, 3, 4, 5, 6])
a = list(range(0, 300000, 3)); b = list(range(1, 300000, 3)); c = list(range(2, 300000, 3))
case("three hundred thousand", merge_three(a, b, c), list(range(300000)))
