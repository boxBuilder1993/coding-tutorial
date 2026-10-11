from solution import is_palindrome
from checker import case
case("with spaces and capitals", is_palindrome("Was it a cat I saw"), True)
case("not a palindrome", is_palindrome("bread"), False)
case("empty", is_palindrome(""), True)
case("single", is_palindrome("a"), True)
