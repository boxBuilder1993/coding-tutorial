from solution import partition_sizes
from checker import case

case("classic", partition_sizes("ababcbacadefegdehijhklij"), [9, 7, 8])
case("all distinct", partition_sizes("abc"), [1, 1, 1])
case("one letter", partition_sizes("aaa"), [3])
case("empty", partition_sizes(""), [])
case("wrapping letter", partition_sizes("abca"), [4])
case("two pieces", partition_sizes("abab" + "cd" + "c"), [4, 3])
