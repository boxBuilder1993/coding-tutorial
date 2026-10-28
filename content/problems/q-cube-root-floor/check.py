from solution import cube_root_floor
from checker import case

case("exact cube", cube_root_floor(27), 3)
case("just above a cube", cube_root_floor(30), 3)
case("zero", cube_root_floor(0), 0)
case("one", cube_root_floor(1), 1)
case("just below a cube", cube_root_floor(63), 3)
case("large exact", cube_root_floor(10 ** 18), 10 ** 6)
case("large inexact", cube_root_floor(10 ** 18 - 1), 999999)
