def solution_part1(input_file):
    with open(input_file, "r") as f:
        numbers = f.readlines()
    sonar_levels = list(map(int, numbers))
    previouws_sonar_level = sonar_levels[0]
    measure_ment = 0
    for i in range(1, len(sonar_levels)):
        current_sonar_level = sonar_levels[i]
        if current_sonar_level > previouws_sonar_level:
            measure_ment += 1
        previouws_sonar_level = current_sonar_level
    return measure_ment


def solution_part2(input_file):
    with open(input_file, "r") as f:
        numbers = f.readlines()
    sonar_levels = list(map(int, numbers))
    previouws_sonar_level = sum(sonar_levels[:3])
    measure_ment = 0
    for i in range(1, len(sonar_levels)-2):
        current_sonar_level = sum(sonar_levels[i:i+3])
        if current_sonar_level > previouws_sonar_level:
            measure_ment += 1
        previouws_sonar_level = current_sonar_level
    return measure_ment


if __name__ == '__main__':
    res_part1 = solution_part1("input.txt")
    print(res_part1)
    res_part2 = solution_part2("input.txt")
    print(res_part2)
