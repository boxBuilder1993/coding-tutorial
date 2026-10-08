from checker import case, output_of_solution
out = output_of_solution().strip()
import solution

case("first now refers to bread", getattr(solution, "first", None), "bread")
case("second now refers to apple", getattr(solution, "second", None), "apple")
case("prints both names", out, "bread apple")
