from solution import count_inversions
from checker import case

case("three inversions", count_inversions([2, 4, 1, 3, 5]), 3)
case("sorted", count_inversions([1, 2, 3]), 0)
case("reversed", count_inversions([3, 2, 1]), 3)
case("empty", count_inversions([]), 0)
case("repeats are not inversions", count_inversions([2, 2, 1]), 2)
n = 20000
case("twenty thousand descending", count_inversions(list(range(n, 0, -1))), n * (n - 1) // 2)
