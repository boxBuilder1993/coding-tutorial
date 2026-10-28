from solution import sort_nearly
from checker import case

case("classic", sort_nearly([6, 5, 3, 2, 8, 10, 9], 3), [2, 3, 5, 6, 8, 9, 10])
case("already sorted", sort_nearly([1, 2, 3], 0), [1, 2, 3])
case("empty", sort_nearly([], 2), [])
case("swap pairs", sort_nearly([2, 1, 4, 3, 6, 5], 1), [1, 2, 3, 4, 5, 6])
case("k larger than length", sort_nearly([3, 1, 2], 10), [1, 2, 3])
big = []
for i in range(0, 100000, 4):
    big.extend([i + 3, i + 1, i + 2, i])
case("a hundred thousand with k of 3", sort_nearly(big, 3), list(range(100000)))
