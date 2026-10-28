from solution import lps
from checker import case

case("bbbab", lps("bbbab"), 4)
case("cbbd", lps("cbbd"), 2)
case("empty", lps(""), 0)
case("single", lps("x"), 1)
case("palindrome", lps("racecar"), 7)
case("all distinct", lps("abcd"), 1)
case("longer", lps("character"), 5)
