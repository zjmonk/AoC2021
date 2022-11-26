def solution_part1(input_file):
    with open(input_file, "r") as f:
        operations = f.readlines()
    xaxis, yaxis = 0, 0
    for instruction in operations:
        op, level = instruction.split(" ")
        level = int(level)
        if op == "forward":
            xaxis += level
        if op == "up":
            yaxis -= level
        if op == "down":
            yaxis += level
    return xaxis*yaxis


def solution_part2(input_file):
    with open(input_file, "r") as f:
        operations = f.readlines()
    aim, xaxis, yaxis = 0, 0, 0
    for instruction in operations:
        op, level = instruction.split(" ")
        level = int(level)
        if op == "forward":
            xaxis += level
            yaxis += aim*level
        if op == "up":
            aim -= level
        if op == "down":
            aim += level
    return xaxis*yaxis
    

if __name__ == '__main__':
    res_part1 = solution_part1("input.txt")
    print(res_part1)
    res_part2 = solution_part2("input.txt")
    print(res_part2)
