from solution import rotate
from checker import case
case("example", rotate([1, 2, 3, 4, 5], 2), [4, 5, 1, 2, 3])
case("k larger than length", rotate([1, 2, 3], 4), [3, 1, 2])
case("k zero", rotate([1, 2, 3], 0), [1, 2, 3])
case("k equals length", rotate([1, 2, 3], 3), [1, 2, 3])
case("empty", rotate([], 5), [])
nums = [1, 2]
case("same list object", rotate(nums, 1) is nums, True)
