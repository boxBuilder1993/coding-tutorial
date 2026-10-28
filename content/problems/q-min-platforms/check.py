from solution import min_platforms
from checker import case

case("classic", min_platforms([900, 940, 950, 1100, 1500, 1800], [910, 1200, 1120, 1130, 1900, 2000]), 3)
case("single", min_platforms([100], [200]), 1)
case("no overlap", min_platforms([1, 3, 5], [2, 4, 6]), 1)
case("all overlap", min_platforms([1, 1, 1], [5, 5, 5]), 3)
case("arrival at departure time needs a new platform", min_platforms([1, 2], [2, 3]), 2)
