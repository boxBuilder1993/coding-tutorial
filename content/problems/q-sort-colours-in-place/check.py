from solution import sort_colours
from checker import case

items = [2, 0, 2, 1, 1, 0]
result = sort_colours(items)
case("sorted in place", items, [0, 0, 1, 1, 2, 2])
case("returns nothing", result, None)
items = []
sort_colours(items)
case("empty", items, [])
items = [1, 1, 1]
sort_colours(items)
case("all ones", items, [1, 1, 1])
items = [2, 2, 0, 0]
sort_colours(items)
case("no ones", items, [0, 0, 2, 2])
items = [(i * 7) % 3 for i in range(100000)]
sort_colours(items)
case("a hundred thousand", items, sorted((i * 7) % 3 for i in range(100000)))
