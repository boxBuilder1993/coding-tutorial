from solution import most_frequent
from checker import case
case("strings", most_frequent(["a", "b", "a", "c", "b", "a"], 2), ["a", "b"])
case("tie by value", most_frequent([3, 1, 3, 1, 2], 2), [1, 3])
case("k is one", most_frequent([5, 5, 6], 1), [5])
case("all distinct", most_frequent([9, 7, 8], 3), [7, 8, 9])
