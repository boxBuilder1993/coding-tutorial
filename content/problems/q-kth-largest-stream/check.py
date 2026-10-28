from solution import kth_largest_stream
from checker import case

case("classic", kth_largest_stream([4, 5, 8, 2], 3), [None, None, 4, 4])
case("k is 1 is running max", kth_largest_stream([3, 1], 1), [3, 3])
case("empty", kth_largest_stream([], 2), [])
case("growing", kth_largest_stream([1, 2, 3, 4], 2), [None, 1, 2, 3])
case("repeats", kth_largest_stream([5, 5, 5], 2), [None, 5, 5])
