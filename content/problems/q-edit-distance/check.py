from solution import edit_distance
from checker import case

case("horse ros", edit_distance("horse", "ros"), 3)
case("intention execution", edit_distance("intention", "execution"), 5)
case("from empty", edit_distance("", "abc"), 3)
case("identical", edit_distance("same", "same"), 0)
case("one replace", edit_distance("cat", "cut"), 1)
case("to empty", edit_distance("abc", ""), 3)
