from solution import insert_position
from checker import case
import bisect

case("between items", insert_position([1, 3, 5, 7], 4), 2)
case("already present", insert_position([1, 3, 5, 7], 5), 2)
case("after the end", insert_position([1, 3, 5, 7], 9), 4)
case("before the start", insert_position([1, 3, 5, 7], 0), 0)
case("empty", insert_position([], 9), 0)
case("first of repeats", insert_position([2, 4, 4, 4, 6], 4), 1)
items = [i * 2 for i in range(100000)]
case("matches bisect_left on a large list", [insert_position(items, t) for t in [0, 1, 777, 199998, 199999, 500000]], [bisect.bisect_left(items, t) for t in [0, 1, 777, 199998, 199999, 500000]])
