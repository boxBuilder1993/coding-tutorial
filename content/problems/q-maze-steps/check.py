from solution import maze_steps
from checker import case

case("small", maze_steps(["S.#", ".##", "..E"]), 4)
case("blocked", maze_steps(["S#E"]), -1)
case("adjacent", maze_steps(["SE"]), 1)
case("detour", maze_steps(["S...", "###.", "E..."]), 8)
case("open field", maze_steps(["S....", ".....", "....E"]), 6)
big = ["S" + "." * 199] + ["." * 200 for _ in range(198)] + ["." * 199 + "E"]
case("two hundred by two hundred", maze_steps(big), 398)
