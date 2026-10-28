from solution import is_palindrome
from checker import case, from_list

case("even palindrome", is_palindrome(from_list([1, 2, 2, 1])), True)
case("not", is_palindrome(from_list([1, 2])), False)
case("empty", is_palindrome(None), True)
case("odd palindrome", is_palindrome(from_list([1, 2, 3, 2, 1])), True)
case("single", is_palindrome(from_list([7])), True)
case("almost", is_palindrome(from_list([1, 2, 3, 1])), False)
