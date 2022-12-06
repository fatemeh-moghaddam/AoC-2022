with open("day02.txt", "rt") as input_file:
    strategy = [line.strip() for line in input_file]

score_table = {'X': 1, 'Y': 2, 'Z': 3}
win = {'A': 'Y', 'B': 'Z', 'C': 'X'}
lose =  {'A': 'Z', 'B': 'X', 'C': 'Y'}
draw =  {'A': 'X', 'B': 'Y', 'C': 'Z'}

def part_1(strategy):
    total = 0
    for round in strategy:
        [elf, me] = round.split()
        total += score_table[me]
        if me == win[elf]:
            total += 6
        elif me == draw[elf]:
            total += 3
    return total

def part_2(strategy):
    total = 0
    for round in strategy:
        [elf, order] = round.split()
        match order:
            case 'X': ## lose
                me = lose[elf]
            case 'Y': ## draw
                me = draw[elf]
                total += 3
            case 'Z': ## win
                me = win[elf]
                total += 6
        total += score_table[me]
    return total

### tests
test_input = ["A Y", "B X", "C Z"]

def test_1():
    assert part_1(test_input) == 15

def test_2():
    assert part_2(test_input) == 12

print(f"part 1: {part_1(strategy)}")
print(f"part 2: {part_2(strategy)}")


