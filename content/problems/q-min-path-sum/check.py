from solution import min_path
from checker import case

case("classic", min_path([[1, 3, 1], [1, 5, 1], [4, 2, 1]]), 7)
case("small", min_path([[1, 2], [1, 1]]), 3)
case("single cell", min_path([[5]]), 5)
case("one row", min_path([[1, 2, 3]]), 6)
case("one column", min_path([[1], [2], [3]]), 6)
grid = [[1] * 100 for _ in range(100)]
case("hundred by hundred", min_path(grid), 199)
