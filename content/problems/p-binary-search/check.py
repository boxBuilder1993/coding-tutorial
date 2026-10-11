from solution import binary_search
from checker import case
case("middle", binary_search([2, 5, 8, 12, 16, 23], 12), 3)
case("absent", binary_search([2, 5, 8], 6), -1)
case("first", binary_search([2, 5, 8], 2), 0)
case("last", binary_search([2, 5, 8], 8), 2)
case("empty", binary_search([], 1), -1)
case("single hit", binary_search([4], 4), 0)
case("single miss", binary_search([4], 3), -1)
case("below all", binary_search([10, 20], 1), -1)
case("above all", binary_search([10, 20], 99), -1)
big = list(range(0, 2000, 2))
case("large list", binary_search(big, 1234), 617)
