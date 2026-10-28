from solution import search_rotated
from checker import case

items = [4, 5, 6, 7, 0, 1, 2]
case("in the second piece", search_rotated(items, 0), 4)
case("absent", search_rotated(items, 3), -1)
case("in the first piece", search_rotated(items, 6), 2)
case("first item", search_rotated(items, 4), 0)
case("last item", search_rotated(items, 2), 6)
case("not rotated", search_rotated([1, 2, 3], 3), 2)
case("empty", search_rotated([], 1), -1)
case("single", search_rotated([5], 5), 0)
big = list(range(600000, 10 ** 6)) + list(range(600000))
case("a million items", [search_rotated(big, t) for t in (0, 599999, 600000, 999999)], [400000, 999999, 0, 399999])
