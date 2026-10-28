from solution import decode_ways
from checker import case

case("12", decode_ways("12"), 2)
case("226", decode_ways("226"), 3)
case("leading zero", decode_ways("06"), 0)
case("single", decode_ways("7"), 1)
case("ten", decode_ways("10"), 1)
case("zero in the middle", decode_ways("100"), 0)
case("long ones", decode_ways("1" * 30), 1346269)
