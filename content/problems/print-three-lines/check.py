from checker import case, output_of_solution

lines = output_of_solution().splitlines()
case("prints exactly three lines", len(lines), 3)
case("first line is apple", lines[0] if len(lines) > 0 else None, "apple")
case("second line is bread", lines[1] if len(lines) > 1 else None, "bread")
case("third line is milk", lines[2] if len(lines) > 2 else None, "milk")
