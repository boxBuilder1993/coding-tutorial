from solution import longest_k_distinct
from checker import case

case("eceba", longest_k_distinct("eceba", 2), 3)
case("aa", longest_k_distinct("aa", 1), 2)
case("whole string", longest_k_distinct("abcabc", 3), 6)
case("k is one", longest_k_distinct("abaccc", 1), 3)
case("empty", longest_k_distinct("", 2), 0)
case("large k", longest_k_distinct("abc", 10), 3)
