from solution import kth_smooth
from checker import case

case("first", kth_smooth(1), 1)
case("seventh", kth_smooth(7), 8)
case("tenth", kth_smooth(10), 12)
case("fifteenth", kth_smooth(15), 24)
case("1500th", kth_smooth(1500), 859963392)
