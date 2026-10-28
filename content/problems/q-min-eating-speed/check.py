from solution import min_speed
from checker import case

case("classic", min_speed([3, 6, 7, 11], 8), 4)
case("one pile per hour", min_speed([30, 11, 23, 4, 20], 5), 30)
case("one spare hour", min_speed([30, 11, 23, 4, 20], 6), 23)
case("plenty of time", min_speed([1, 1, 1], 100), 1)
case("single pile", min_speed([10], 3), 4)
case("many piles", min_speed(list(range(1, 10001)), 20000), 3334)
