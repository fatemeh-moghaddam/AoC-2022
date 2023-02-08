def sum_cal(input_file):
    elf_num = 0
    elves = [0]
    for line in input_file:
        if line == "\n":
            elf_num += 1
            line = next(input_file)
            elves.append(0)         # to start adding directly in the next line
        elves[elf_num] += int(line)
    elves.sort(reverse= True)
    return max(elves), sum(elves[:3])


with open("day01.txt", "rt") as input_file:
    part_1, part_2 = sum_cal(input_file)
    print(f"The most total calories of one elf is {part_1}")
    print(f"The sum of top three is {part_2}")

with open("test_day01", "rt") as test_file:
    part_1, part_2 = sum_cal(test_file)

def test_1():
    assert part_1 == 24000

def test_2():
    assert part_2 == 45000
