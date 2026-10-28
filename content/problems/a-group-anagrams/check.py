from solution import group_anagrams
from checker import case

case("classic", group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]), [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]])
case("empty", group_anagrams([]), [])
case("no anagrams", group_anagrams(["a", "b"]), [["a"], ["b"]])
case("all anagrams", group_anagrams(["abc", "bca", "cab"]), [["abc", "bca", "cab"]])
case("empty strings group together", group_anagrams(["", "x", ""]), [["", ""], ["x"]])
case("repeated letters matter", group_anagrams(["aab", "aba", "abb"]), [["aab", "aba"], ["abb"]])
