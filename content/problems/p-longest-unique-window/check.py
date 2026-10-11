from solution import longest_unique
from checker import case
case("example", longest_unique("abcabcbb"), 3)
case("all same", longest_unique("bbbbb"), 1)
case("empty", longest_unique(""), 0)
case("all distinct", longest_unique("abcdef"), 6)
case("repeat far back", longest_unique("abba"), 2)
