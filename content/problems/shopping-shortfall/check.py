from solution import shortfall
from checker import case

case("missing some", shortfall(["egg", "egg", "egg", "milk"], ["egg", "butter"]), {"egg": 2, "milk": 1})
case("fully covered", shortfall(["egg"], ["egg", "egg"]), {})
case("empty kitchen", shortfall(["milk", "milk"], []), {"milk": 2})
case("nothing needed", shortfall([], ["egg"]), {})
case("extras in the kitchen are ignored", shortfall(["flour"], ["egg", "milk", "flour"]), {})
