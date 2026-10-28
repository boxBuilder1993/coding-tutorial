from solution import max_island
from checker import case

case("three cells", max_island(["110", "010", "001"]), 3)
case("no land", max_island(["000"]), 0)
case("all land", max_island(["11", "11"]), 4)
case("two islands, pick bigger", max_island(["1100", "0000", "0111"]), 3)
case("empty grid", max_island([]), 0)
case("diagonal not connected", max_island(["10", "01"]), 1)
