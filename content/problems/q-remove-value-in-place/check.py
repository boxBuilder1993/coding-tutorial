from solution import remove_value
from checker import case

items = [3, 2, 2, 3]
k = remove_value(items, 3)
case("count", k, 2)
case("front of list", items[:k], [2, 2])
items = [0, 1, 2, 2, 3, 0, 4, 2]
k = remove_value(items, 2)
case("longer count", k, 5)
case("longer front", items[:k], [0, 1, 3, 0, 4])
items = []
case("empty", remove_value(items, 1), 0)
items = [1, 1]
case("everything removed", remove_value(items, 1), 0)
items = [5, 6]
k = remove_value(items, 9)
case("nothing removed", (k, items[:k]), (2, [5, 6]))
