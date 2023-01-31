with open("day09.txt", "rt") as input_file:
    inputs = [line.strip() for line in input_file]


# Based on Planck lengths rules; 
# diagonally adjacent and even overlapping both count as touching
# input is a head position, and output is a set of allowed positions for tail
def allowed_pos(pos):
    x,y = pos
    allowed = set()
    for i in range(-1,2):
        for j in range(-1,2):
            allowed.add((x+i,y+j))
    return allowed



def move_head(pos, dir):
    x, y = pos
    orientation = {'U': (1,0), 'D': (-1,0), 'R': (0,1), 'L':(0,-1)}
    i, j = orientation[dir]
    pos = (x+i, y+j)
    return pos


# output is the new position of the tail
def move_tail(pos, head_pos):
    x, y = pos
    hx, hy = head_pos
    delta_x, delta_y = hx-x, hy-y
    # we want to move diagonaly if there was a diagonal difference, 
    # but we will only take one step at a time, so it should be divided by the amplitude 
    # also, we need to keep the direction, so divide by the absolute of amplitude
    if delta_x != 0: xmove = delta_x//abs(delta_x)
    else: xmove = 0
    if delta_y != 0: ymove = delta_y//abs(delta_y)
    else: ymove = 0
    pos = (x + xmove, y + ymove)
    return pos



## part 1
# input is not splitted yet
def safe_rope(movements):
    head_pos = (0,0)
    tail_pos = (0,0)
    # at first I initialized this with (0,0), but for some reason that I don't know,
    # it stored that as 0 and it stores (0,0) at some point, 
    # so the number of length was one more than it should
    seen = set()
    for action in movements:
        [dir, steps] = action.split()
        # move head one step, check tail, move tail if needed,
        # do this until all steps are done
        for _ in range(int(steps)):
            head_pos = move_head(head_pos, dir)
            if tail_pos not in allowed_pos(head_pos):
                tail_pos = move_tail(tail_pos, head_pos)
                seen.add(tail_pos)
    # print((0,0) in seen)
    return seen


## part 2
def long_rope(movements):
    knots = [(0,0) for _ in range(10)]
    seen_target = [set(knots[i]) for i in range(10)]
    for action in movements:
        [dir, steps] = action.split()
        for _ in range(int(steps)):
            # this is the head
            knots[0] = move_head(knots[0], dir)
            seen_target[0].add(knots[0])
            # move first knot based on head, then
            # move each tail based on the tail knot before it
            for i in range(1,10):
                if knots[i] not in allowed_pos(knots[i-1]):
                    knots[i] = move_tail(knots[i], knots[i-1])
                    seen_target[i].add(knots[i])
    return seen_target



# for visualization
def visualize(seen, dims):
    r, c = dims
    locations = {0:[0]}
    for s in list(seen):
        if s!=0:
            x, y = s
            if x in locations:
                locations[x].append(y)
            else: locations[x] = [y]
    display = ''
    for i in range(r//2, -r//2, -1):
        display += '\n'
        for j in range(-c//2, c//2, 1):
            if i in locations and j in locations[i]:
                display += '#'
            else:
                display += '.'
    print(display)



test_input = ['R 4',
'U 4',
'L 3',
'D 1',
'R 4',
'D 1',
'L 5',
'R 2']

test_input2 = ['R 5', 'U 8', 'L 8','D 3', 'R 17', 'D 10', 'L 25', 'U 20']




# part 1
print("Part 1: ", len(safe_rope(inputs)))
# part 2
seen = long_rope(inputs)
print("Part 2: ", len(seen[-1]))



# seen_test2 = long_rope(test_input2)
# visualize(safe_rope(test_input), (10,20))
# visualize(seen_test2[-1], (20,40))

