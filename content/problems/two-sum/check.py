from solution import two_sum
from checker import case


def valid_pair(nums, target):
    def check(actual, _expected):
        if not isinstance(actual, (list, tuple)) or len(actual) != 2:
            return False
        i, j = actual
        return i != j and nums[i] + nums[j] == target
    return check


case("example", two_sum([2, 7, 11, 15], 9), [0, 1], compare="sorted")
case("pair at end", two_sum([3, 2, 4], 6), [1, 2], compare="sorted")
case("duplicates needed", two_sum([3, 3], 6), [0, 1], compare="sorted")
case("negatives", two_sum([-1, -2, -3, -4, -5], -8), [2, 4], compare="sorted")
case("does not reuse an element", two_sum([1, 4, 5, 3], 8), "a valid pair", compare=valid_pair([1, 4, 5, 3], 8))
