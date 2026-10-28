from solution import boats
from checker import case

case("one boat", boats([1, 2], 3), 1)
case("three boats", boats([3, 2, 2, 1], 3), 3)
case("everyone alone", boats([3, 5, 3, 4], 5), 4)
case("empty", boats([], 10), 0)
case("all pair up", boats([1, 1, 1, 1], 2), 2)
case("one person", boats([7], 7), 1)
