from solution import all_breaks
from checker import case

case("two ways", all_breaks("catsanddog", ["cat", "cats", "and", "sand", "dog"]), ["cats and dog", "cat sand dog"], compare="sorted")
case("three ways", all_breaks("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]), ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"], compare="sorted")
case("none", all_breaks("catsandog", ["cats", "dog", "sand", "and", "cat"]), [], compare="sorted")
case("single word", all_breaks("a", ["a"]), ["a"], compare="sorted")
case("count with repeats", len(all_breaks("aaaa", ["a", "aa"])), 5)
