from solution import compress
from checker import case
case("runs", compress("aaabccdddd"), "a3bc2d4")
case("no runs", compress("abc"), "abc")
case("empty", compress(""), "")
case("single run", compress("zzzz"), "z4")
case("run at the end", compress("abb"), "ab2")
