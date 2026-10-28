from solution import relative_sort
from checker import case

case("classic", relative_sort([2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6]), [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19])
case("nothing in order", relative_sort([3, 1, 2], []), [1, 2, 3])
case("everything in order", relative_sort([3, 1, 2], [3, 2, 1]), [3, 2, 1])
case("empty items", relative_sort([], [1]), [])
case("strings", relative_sort(["b", "c", "a", "d"], ["c", "a"]), ["c", "a", "b", "d"])
