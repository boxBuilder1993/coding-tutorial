from solution import matches
from checker import case

case("too short", matches("aa", "a"), False)
case("star", matches("aa", "a*"), True)
case("dot star", matches("ab", ".*"), True)
case("zero of c", matches("aab", "c*a*b"), True)
case("mississippi", matches("mississippi", "mis*is*p*."), False)
case("empty both", matches("", ""), True)
case("empty text with stars", matches("", "a*b*"), True)
case("dot needs a character", matches("", "."), False)
case("mississippi success", matches("mississippi", "mis*is*ip*."), True)
