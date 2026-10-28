from solution import ladder_length
from checker import case

case("classic", ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]), 5)
case("no end word", ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log"]), 0)
case("one step", ladder_length("a", "c", ["a", "b", "c"]), 2)
case("already there", ladder_length("abc", "abc", ["abc"]), 1)
case("unreachable", ladder_length("aaa", "zzz", ["zzz"]), 0)
case("choose the shorter", ladder_length("ab", "cd", ["ad", "cd", "cb", "xb"]), 3)
