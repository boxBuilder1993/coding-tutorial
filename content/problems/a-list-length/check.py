from solution import length
from checker import case, from_list

case("three nodes", length(from_list([1, 2, 3])), 3)
case("empty", length(None), 0)
case("one node", length(from_list(["apple"])), 1)
case("a thousand nodes", length(from_list(range(1000))), 1000)
