with open("day09.txt", "rt") as input_file:
    inputs = [line.strip() for line in input_file]


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


def move_tail(pos, head_pos, seen):
    x, y = pos
    hx, hy = head_pos
    delta_x, delta_y = hx-x, hy-y
    if delta_x != 0: xmove = delta_x//abs(delta_x)
    else: xmove = 0
    if delta_y != 0: ymove = delta_y//abs(delta_y)
    else: ymove = 0
    pos = (x + xmove, y + ymove)
    seen.add(pos)
    return pos

# part 1
def safe_rope(movements):
    head_pos = (0,0)
    tail_pos = (0,0)
    seen = set(tail_pos)
    for action in movements:
        [dir, steps] = action.split()
        for _ in range(int(steps)):
            head_pos = move_head(head_pos, dir)
            if tail_pos not in allowed_pos(head_pos):
                tail_pos = move_tail(tail_pos, head_pos, seen)
    return seen

# part 2
def long_rope(movements):
    knots = [(0,0) for _ in range(10)]
    seen_target = [set(knots[i]) for i in range(10)]
    for action in movements:
        [dir, steps] = action.split()
        for _ in range(int(steps)):
            knots[0] = move_head(knots[0], dir)
            seen_target[0].add(knots[0])
            for i in range(1,10):
                if knots[i] not in allowed_pos(knots[i-1]):
                    knots[i] = move_tail(knots[i], knots[i-1], seen_target[i])
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
print(len(safe_rope(inputs)))
# part 2
seen = long_rope(inputs)
print(len(seen[-1]))



# seen_test2 = long_rope(test_input2)
# visualize(safe_rope(test_input), (10,20))
# visualize(seen_test2[-1], (20,40))

