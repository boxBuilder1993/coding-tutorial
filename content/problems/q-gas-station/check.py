from solution import start_station
from checker import case

case("classic", start_station([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]), 3)
case("impossible", start_station([2, 3, 4], [3, 4, 3]), -1)
case("start at zero", start_station([3, 1, 1], [1, 2, 2]), 0)
case("single station", start_station([1], [1]), 0)
case("last station", start_station([1, 1, 5], [3, 2, 2]), 2)
