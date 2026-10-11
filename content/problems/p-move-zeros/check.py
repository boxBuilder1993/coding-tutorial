from solution import move_zeros
from checker import case
case("example", move_zeros([0, 1, 0, 3, 12]), [1, 3, 12, 0, 0])
case("no zeros", move_zeros([1, 2]), [1, 2])
case("all zeros", move_zeros([0, 0]), [0, 0])
case("empty", move_zeros([]), [])
nums = [0, 5]
result = move_zeros(nums)
case("same list object", result is nums, True)
