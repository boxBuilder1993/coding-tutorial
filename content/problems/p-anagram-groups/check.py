from solution import anagram_groups
from checker import case
case("classic", anagram_groups(["tea", "eat", "tan", "ate", "nat", "bat"]), [["bat"], ["tan", "nat"], ["tea", "eat", "ate"]])
case("empty", anagram_groups([]), [])
case("no anagrams", anagram_groups(["b", "a"]), [["a"], ["b"]])
