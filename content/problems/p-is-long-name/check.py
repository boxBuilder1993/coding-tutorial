from solution import is_long
from checker import case
case("long", is_long("sourdough bread"), True)
case("short", is_long("milk"), False)
case("exactly ten is not long", is_long("abcdefghij"), False)
