from solution import grid_paths
from checker import case

case("single cell", grid_paths(1, 1), 1)
case("two by two", grid_paths(2, 2), 2)
case("three by three", grid_paths(3, 3), 6)
case("three by seven", grid_paths(3, 7), 28)
case("one row", grid_paths(1, 9), 1)
case("eighteen by eighteen", grid_paths(18, 18), 2333606220)
case("wide", grid_paths(2, 50), 50)
