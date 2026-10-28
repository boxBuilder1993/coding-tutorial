from solution import can_break
from checker import case

case("leetcode", can_break("leetcode", ["leet", "code"]), True)
case("reuse", can_break("applepenapple", ["apple", "pen"]), True)
case("catsandog", can_break("catsandog", ["cats", "dog", "sand", "and", "cat"]), False)
case("empty text", can_break("", ["a"]), True)
case("no words", can_break("a", []), False)
case("overlapping choices", can_break("aaaaab", ["a", "aa", "aaa"]), False)
