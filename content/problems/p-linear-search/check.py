from solution import linear_search
from checker import case
case("middle", linear_search(["milk", "bread", "eggs"], "bread"), 1)
case("absent", linear_search(["milk"], "eggs"), -1)
case("first of duplicates", linear_search([1, 2, 1], 1), 0)
case("empty", linear_search([], 1), -1)
case("last position", linear_search([5, 6, 7], 7), 2)
