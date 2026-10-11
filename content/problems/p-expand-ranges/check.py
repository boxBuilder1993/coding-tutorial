from solution import expand
from checker import case
case("mixed", expand("3-5, 8, 10-11"), [3, 4, 5, 8, 10, 11])
case("single", expand("7"), [7])
case("range of one", expand("4-4"), [4])
case("no spaces", expand("1-2,9"), [1, 2, 9])
