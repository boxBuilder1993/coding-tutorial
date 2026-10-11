from solution import bubble_sort
from checker import case
case("example", bubble_sort([5, 1, 4, 2]), [1, 2, 4, 5])
case("empty", bubble_sort([]), [])
case("single", bubble_sort([1]), [1])
case("already sorted", bubble_sort([1, 2, 3]), [1, 2, 3])
case("reversed", bubble_sort([3, 2, 1]), [1, 2, 3])
case("duplicates", bubble_sort([2, 1, 2, 1]), [1, 1, 2, 2])
nums = [9, 8, 7]
bubble_sort(nums)
case("sorts in place", nums, [7, 8, 9])
