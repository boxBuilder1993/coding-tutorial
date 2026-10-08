from checker import case, output_of_solution
out = output_of_solution().strip()
import solution

case("stock is 7 afterwards", getattr(solution, "stock", None), 7)
case("prints 7", out, "7")
