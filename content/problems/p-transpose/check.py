from solution import transpose
from checker import case
case("two by three", transpose([[1, 2, 3], [4, 5, 6]]), [[1, 4], [2, 5], [3, 6]])
case("empty", transpose([]), [])
case("one row", transpose([[1, 2]]), [[1], [2]])
case("square", transpose([[1, 2], [3, 4]]), [[1, 3], [2, 4]])
