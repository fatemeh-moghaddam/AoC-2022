with open("day03.txt", "rt") as input_file:
    rucksacks = [line.strip() for line in input_file]


def priority(char):
    if char.isupper(): 
        return ord(char)-38     # Lowercase item types have priorities 1 through 26.
    else:
        return ord(char)-96     # Uppercase item types have priorities 27 through 52.

def disjoint(set1, set2):
    return set1 - (set1 - set2)

def reorganization(sacks):
    items = []      # for part 1
    badges = []     # for part 2
    count = 0
    for i, rucksack in enumerate(sacks):
        count += 1
        
        n = len(rucksack)
        comp1 = set(rucksack[: n//2])
        comp2 = set(rucksack[n//2 :])
        item_set = disjoint(comp1, comp2)
        item = item_set.pop()
        items.append(priority(item))
        
        # for part 2:
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



