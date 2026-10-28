from solution import fewest_coins
from checker import case

case("greedy would say 6", fewest_coins(30, [25, 10, 1]), 3)
case("standard coins", fewest_coins(67, [25, 10, 5, 1]), 6)
case("impossible", fewest_coins(3, [2]), -1)
case("zero amount", fewest_coins(0, [7]), 0)
case("single coin type", fewest_coins(9, [3]), 3)
case("unsorted coins", fewest_coins(11, [1, 5, 2]), 3)
case("larger amount", fewest_coins(10000, [7, 11, 13]), 770)
