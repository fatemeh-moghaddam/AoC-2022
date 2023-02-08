import re
with open("day05.txt", "rt") as input_file:
    crates = input_file.readlines()


def rearrangement(crates):
    stacks = [[] for i in range(9)] # we have 9 stacks
    part_1 = ''
    part_2 = ''
    flag = True
    for line in crates:
        if line == "\n": continue
        if line.find("move") == -1:
            ## this is the positions of crates
            positions = [(pos.start()+1) for pos in re.finditer('\[', line)]
            # there are 4 spaces between columns in the input file 
            columns = [p//4 for p in positions]
            for i in range(len(columns)):
                stacks[columns[i]].append(line[positions[i]])
        else:
            if flag: # to reverse the stack once
                flag = False
                stacks2 = [s[::-1] for s in stacks]
                stacks = [s[::-1] for s in stacks]
            ## extract numbers from instructions
            [boxes, fr, to] = list(map(int, re.findall('[0-9]+', line)))
            n = len(stacks2[fr-1]) # length of the target stack
            for _ in range(boxes):
                stacks[to-1].append(stacks[fr-1].pop())             # append in the same order you pop
                stacks2[to-1].append(stacks2[fr-1].pop(n-boxes))    # append as you popped all first, then appended
                # can be done with a temp also
                
    for s1, s2 in zip(stacks, stacks2):
        part_1 += s1.pop()
        part_2 += s2.pop()
    return part_1, part_2
        

### tests
test_input = ["    [D] ",
"[N] [C] ",
"[Z] [M] [P]",
 " 1   2   3 ", 
 "move 1 from 2 to 1",
 "move 3 from 1 to 3",
 "move 2 from 2 to 1",
 "move 1 from 1 to 2 "]
   



print(rearrangement(crates))
