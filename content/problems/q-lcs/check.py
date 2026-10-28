from solution import lcs
from checker import case

case("ace", lcs("abcde", "ace"), 3)
case("nothing shared", lcs("abc", "def"), 0)
case("empty", lcs("", "abc"), 0)
case("identical", lcs("abc", "abc"), 3)
case("repeats", lcs("aab", "azb"), 2)
case("longer", lcs("AGGTAB", "GXTXAYB"), 4)
