from solution import kth_smallest
from checker import case

case("fourth", kth_smallest([[1, 5, 9], [2, 3], [4]], 4), 4)
case("repeats", kth_smallest([[1, 1], [1]], 3), 1)
case("first", kth_smallest([[3], [1], [2]], 1), 1)
case("last", kth_smallest([[3], [1], [2]], 3), 3)
case("some empty lists", kth_smallest([[], [5, 6], []], 2), 6)
lists = [list(range(i, 100000, 50)) for i in range(50)]
case("fifty long lists", kth_smallest(lists, 77777), 77776)
