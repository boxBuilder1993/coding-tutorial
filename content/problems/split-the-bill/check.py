from checker import case, output_of_solution

lines = output_of_solution().splitlines()
case("prints three lines", len(lines), 3)
case("share per person", lines[0] if len(lines) > 0 else None, "25.0")
case("full boxes", lines[1] if len(lines) > 1 else None, "3")
case("eggs left over", lines[2] if len(lines) > 2 else None, "2")
