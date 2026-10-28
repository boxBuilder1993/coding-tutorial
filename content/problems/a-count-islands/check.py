from solution import count_islands
from checker import case

case("three islands", count_islands(["11000", "11000", "00100", "00011"]), 3)
case("all water", count_islands(["000"]), 0)
case("all land", count_islands(["111", "111"]), 1)
case("diagonals do not connect", count_islands(["10", "01"]), 2)
case("empty grid", count_islands([]), 0)
case("ring shape", count_islands(["111", "101", "111"]), 1)
case("checkerboard", count_islands(["1010", "0101", "1010"]), 6)
big = ["1" * 300 if r % 2 == 0 else "0" * 300 for r in range(300)]
case("a large striped grid", count_islands(big), 150)
