from solution import min_window
from checker import case

case("classic", min_window("ADOBECODEBANC", "ABC"), "BANC")
case("not enough copies", min_window("a", "aa"), "")
case("exact", min_window("abc", "cba"), "abc")
case("repeats needed", min_window("aaabbbccc", "abcc"), "abbbcc")
case("leftmost tie", min_window("abxab", "ab"), "ab")
case("empty letters", min_window("abc", ""), "")
big = ("xyz" * 33333) + "abc"
case("a hundred thousand", min_window(big, "cab"), "abc")
