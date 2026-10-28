from solution import paths
from checker import case

case("one obstacle", paths([[0, 0, 0], [0, 1, 0], [0, 0, 0]]), 2)
case("small", paths([[0, 1], [0, 0]]), 1)
case("start blocked", paths([[1]]), 0)
case("no obstacles", paths([[0, 0, 0], [0, 0, 0]]), 3)
case("wall across", paths([[0, 0], [1, 1], [0, 0]]), 0)
case("end blocked", paths([[0, 0], [0, 1]]), 0)
