from solution import flood_fill
from checker import case

case("classic", flood_fill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2), [[2, 2, 2], [2, 2, 0], [2, 0, 1]])
case("same colour", flood_fill([[0, 0]], 0, 0, 0), [[0, 0]])
case("single cell", flood_fill([[5]], 0, 0, 9), [[9]])
case("isolated start", flood_fill([[1, 0], [0, 1]], 0, 0, 3), [[3, 0], [0, 1]])
img = [[1, 1], [1, 1]]
result = flood_fill(img, 0, 0, 7)
case("in place", result is img and img == [[7, 7], [7, 7]], True)
