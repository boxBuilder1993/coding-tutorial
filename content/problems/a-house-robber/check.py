from solution import most_cash
from checker import case

case("skip the middle", most_cash([2, 7, 9, 3, 1]), 12)
case("alternate", most_cash([1, 2, 3, 1]), 4)
case("empty street", most_cash([]), 0)
case("one house", most_cash([5]), 5)
case("two houses", most_cash([5, 9]), 9)
case("take the middle only", most_cash([1, 100, 1]), 100)
case("a hundred thousand houses", most_cash([3] * 100000), 150000)
