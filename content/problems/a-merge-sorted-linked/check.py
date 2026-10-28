from solution import merge
from checker import case, from_list, to_list

case("interleaved", to_list(merge(from_list([1, 3, 5]), from_list([2, 3, 6]))), [1, 2, 3, 3, 5, 6])
case("first empty", to_list(merge(None, from_list([4, 7]))), [4, 7])
case("second empty", to_list(merge(from_list([4, 7]), None)), [4, 7])
case("both empty", merge(None, None), None)
case("all of a before b", to_list(merge(from_list([1, 2]), from_list([3, 4]))), [1, 2, 3, 4])
a = from_list([1, 4])
b = from_list([2])
merged = merge(a, b)
case("reuses nodes", merged is a and merged.next is b, True)
