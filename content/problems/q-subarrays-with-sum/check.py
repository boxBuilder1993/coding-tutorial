from solution import count_runs
from checker import case

case("ones", count_runs([1, 1, 1], 2), 2)
case("two ways", count_runs([1, 2, 3], 3), 2)
case("zeros with negatives", count_runs([1, -1, 1, -1], 0), 4)
case("empty", count_runs([], 0), 0)
case("whole list", count_runs([5, 5], 10), 1)
case("none", count_runs([1, 2], 7), 0)
big = [1] * 100000
case("a hundred thousand ones", count_runs(big, 3), 99998)
