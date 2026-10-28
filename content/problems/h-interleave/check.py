from solution import is_interleaving
from checker import case

case("yes", is_interleaving("aabcc", "dbbca", "aadbbcbcac"), True)
case("no", is_interleaving("aabcc", "dbbca", "aadbbbaccc"), False)
case("all empty", is_interleaving("", "", ""), True)
case("length mismatch", is_interleaving("a", "b", "abc"), False)
case("needs the table", is_interleaving("ab", "ac", "aabc"), True)
case("one empty", is_interleaving("", "abc", "abc"), True)
