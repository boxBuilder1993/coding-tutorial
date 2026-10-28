from solution import longest_zero_run
from checker import case

case("six long", longest_zero_run([1, -1, 3, 2, -2, -3, 3]), 6)
case("none", longest_zero_run([1, 2, 3]), 0)
case("all zeros", longest_zero_run([0, 0, 0]), 3)
case("empty", longest_zero_run([]), 0)
case("whole list", longest_zero_run([2, -2]), 2)
case("ends with zero sum", longest_zero_run([5, 1, -1]), 2)
