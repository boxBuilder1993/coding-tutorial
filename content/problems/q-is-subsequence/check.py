from solution import is_subsequence
from checker import case

case("ace in abcde", is_subsequence("ace", "abcde"), True)
case("order matters", is_subsequence("aec", "abcde"), False)
case("empty small", is_subsequence("", "abc"), True)
case("empty big", is_subsequence("a", ""), False)
case("identical", is_subsequence("abc", "abc"), True)
case("repeats needed", is_subsequence("aa", "a"), False)
