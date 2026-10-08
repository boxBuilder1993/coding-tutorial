from checker import case, output_of_solution
out = output_of_solution().strip()
import solution

case("item refers to the text bread", getattr(solution, "item", None), "bread")
case("prints the line", out, "You bought bread")
