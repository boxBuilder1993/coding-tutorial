from solution import k_closest
from checker import case

case("two of three", k_closest([(3, 3), (5, -1), (-2, 4)], 2), [(3, 3), (-2, 4)])
case("one of two", k_closest([(1, 3), (-2, 2)], 1), [(-2, 2)])
case("all of them", k_closest([(2, 0), (0, 1)], 2), [(0, 1), (2, 0)])
case("origin itself", k_closest([(0, 0), (1, 1)], 1), [(0, 0)])
case("negatives", k_closest([(-5, 0), (3, 0), (0, -4)], 2), [(3, 0), (0, -4)])
pts = [((i * 37) % 1001 - 500, (i * 53) % 1003 - 501) for i in range(20000)]
pts = list({(x, y): None for x, y in pts})
expected = sorted(pts, key=lambda p: (p[0] ** 2 + p[1] ** 2, p))[:10]
case("twenty thousand points", sorted(k_closest(pts, 10), key=lambda p: (p[0] ** 2 + p[1] ** 2, p)), expected)
