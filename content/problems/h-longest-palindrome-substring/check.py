from solution import longest_palindrome
from checker import case

case("odd", longest_palindrome("babad"), "bab")
case("even", longest_palindrome("cbbd"), "bb")
case("empty", longest_palindrome(""), "")
case("single", longest_palindrome("x"), "x")
case("whole", longest_palindrome("racecar"), "racecar")
case("leftmost tie", longest_palindrome("abcd"), "a")
case("long run", longest_palindrome("ab" + "c" * 3000 + "ba"), "ab" + "c" * 3000 + "ba")
