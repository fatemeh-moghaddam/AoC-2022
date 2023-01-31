
# this will add the rocks in an interval to the cave dict
def add(cor1, cor2, cave):
    (x1,y1) , (x2,y2) = cor1, cor2
    # print(f"{cor1=}, {cor2=}")
    if y2 > y1:
        for y in range(y1, y2+1):
            cave[(x1, y)] = '#'
    if y2 < y1:
        for y in range(y2, y1+1):
            cave[(x1, y)] = '#'
    if x2 > x1:
        for x in range(x1, x2+1):
            cave[(x, y1)] = '#'
    if x2 < x1:
        for x in range(x2, x1+1):
            cave[(x, y1)] = '#'
    return cave, max(y1, y2)


# this will read the cave from the strings of paths and turn it into cave dict,
# with the help of add function
def read_cave(my_input):
    cave = dict()
    wall = 0
    for line in my_input:
        # to get the coordinates seperately
        path = []
        for pair in line.split("->"):
            # to have the path as a list of coordinates
            path.append(tuple(map(int, pair.split(","))))
        for i in range(len(path)-1):
            cave, new_wall = add(path[i], path[i+1], cave)
            # there will be a horizontal wall, so there will be a 
            wall = max(new_wall, wall)
    return cave, wall


# this will generate falling of a sand pattern
def fall(cave, pos):
    xs, ys = pos
    if (xs, ys+1) not in cave: # down one step
        yield (xs, ys+1)
    elif (xs-1, ys+1) not in cave: # one step down and to the left
        yield (xs-1, ys+1)
    elif (xs+1, ys+1) not in cave: # one step down and to the right
        yield (xs+1, ys+1)
    else: # all were full
        yield (0,0)



# this is for part 1
def reservoir(path_map):
    cave, wall = read_cave(path_map)
    ys = 0
    count = 0
    while ys < wall:
        # reset the starting position
        pos = (500,0)
        count += 1
        while pos != (0,0) and ys < wall: # because we return (0,0) when it's full
            prev = pos
            (xs, ys) = prev
            pos = next(fall(cave, pos))
        # it means that the sand came to rest, or abyss started
        cave[prev] = 'o'
    # visualize(cave, (15,20))
    return count-1



# this is for part 2
def pile(path_map):
    cave, wall = read_cave(path_map)

    prev = (0,0)
    count = 0
    while prev != (500,0):
        # reset the starting position
        ys = 0
        pos = (500,0)
        while pos != (0,0) and ys < wall + 2:
            prev = pos
            (xs, ys) = prev
            pos = next(fall(cave, pos))
        # it means that the sand came to rest, or abyss started
        if ys == wall + 2:
            cave[prev] = '#'
        else:
            count += 1
            cave[prev] = 'o'
    return count



# for visualization
def visualize(cave, dims):
    r, c = dims
    display = ''
    for x in range(c):
        display += '\n'
        for y in range(r):
            # print((x+490, y))
            if (x+485, y) in cave:
                display += cave[(x+485, y)]
            else:
                display += '.'
    print(display)




## inputs
test = ["498,4 -> 498,6 -> 496,6", "503,4 -> 502,4 -> 502,9 -> 494,9"]
with open("day14.txt", "rt") as my_file:
    my_input = my_file.readlines()



## for visualization:
cave , wall = read_cave(test)
# visualize(cave, (15,30))


def main(paths):
    print(f"Part 1: {reservoir(paths)}")
    print(f"Part 2: {pile(paths)}")
    return

main(test)
main(my_input)


