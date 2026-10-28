from solution import reverse_vowels
from checker import case

case("hello", reverse_vowels("hello"), "holle")
case("leetcode", reverse_vowels("leetcode"), "leotcede")
case("no vowels", reverse_vowels("xyz"), "xyz")
case("empty", reverse_vowels(""), "")
case("capitals", reverse_vowels("Apple"), "epplA")
case("all vowels", reverse_vowels("aeiou"), "uoiea")
