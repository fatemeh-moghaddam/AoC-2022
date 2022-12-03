with open("day03.txt", "rt") as input_file:
    rucksacks = [line.strip() for line in input_file]


def priority(char):
    if char.isupper():
        return ord(char)-38
    else:
        return ord(char)-96

def disjoint(set1, set2):
    return set1 - (set1 - set2)

def reorganization(sacks):
    items = []
    badges = []
    count = 0
    for i, rucksack in enumerate(sacks):
        count += 1
        n = len(rucksack)
        comp1 = set(rucksack[: n//2])
        comp2 = set(rucksack[n//2 :])
        item_set = disjoint(comp1, comp2)
        item = item_set.pop()
        items.append(priority(item))
        if count == 3:
            count = 0
            badge_set = disjoint(set(sacks[i]), disjoint(set(sacks[i-1]), set(sacks[i-2])))
            badge = badge_set.pop()
            badges.append(priority(badge))
    return sum(items), sum(badges)


### tests
test_input = ["vJrwpWtwJgWrhcsFMMfFFhFp",
 "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", 
 "PmmdzqPrVvPwwTWBwg", 
 "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
 "ttgJtRGJQctTZtZT",
 "CrZsJsPPZsGzwwsLwLmpwMDw"]

part_1 , part_2 = reorganization(test_input)

def test_1():
    assert part_1 == 157

def test_2():
        assert part_2 == 70

print(reorganization(rucksacks))



