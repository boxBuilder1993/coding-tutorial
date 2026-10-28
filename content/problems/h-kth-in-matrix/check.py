from solution import kth_smallest
from checker import case

m = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
case("eighth", kth_smallest(m, 8), 13)
case("single", kth_smallest([[-5]], 1), -5)
case("first", kth_smallest(m, 1), 1)
case("last", kth_smallest(m, 9), 15)
case("repeats", kth_smallest([[1, 2], [1, 3]], 2), 1)
n = 300
big = [[r + c for c in range(n)] for r in range(n)]
flat = sorted(v for row in big for v in row)
case("three hundred square", kth_smallest(big, 44444), flat[44443])
