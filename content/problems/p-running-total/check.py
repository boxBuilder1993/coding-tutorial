from solution import running
from checker import case
case("three", running([10, 5, 20]), [10, 15, 35])
case("empty", running([]), [])
case("negatives", running([5, -5, 5]), [5, 0, 5])
