from solution import balanced
from checker import case

case("one pair", balanced(1), ["()"], compare="sorted")
case("two pairs", balanced(2), ["(())", "()()"], compare="sorted")
case("three pairs", balanced(3), ["((()))", "(()())", "(())()", "()(())", "()()()"], compare="sorted")
case("zero", balanced(0), [""], compare="sorted")
case("count for six", len(balanced(6)), 132)
