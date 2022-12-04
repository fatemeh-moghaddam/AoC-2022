import re

with open("day04.txt", "rt") as input_file:
    assignments = [line.strip() for line in input_file]



def cleanup(assignments):
    count = 0
    overlap = 0
    for sections in assignments:
        [s1, e1, s2, e2] = list(map(int, re.split("-|,", sections)))
        if (s2 > e1) or (s1 > e2): continue
        if (s2 < s1 and e2 < e1) or (s1 < s2 and e1 < e2): 
            overlap += 1
            continue
        count += 1
    return count, overlap + count








### tests
test_input = ["2-4,6-8",
 "2-3,4-5", 
 "5-7,7-9",
 "2-8,3-7",
 "6-6,4-6",
 "2-6,4-8"]


part_1 , part_2 = cleanup(test_input)

def test_1():
    assert part_1 == 2

def test_2():
    assert part_2 == 4

print(cleanup(assignments))

