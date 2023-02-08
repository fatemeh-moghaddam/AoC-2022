import numpy as np

with open("day08.txt", "rt") as input_file:
    forest = [line.strip() for line in input_file]

# Input of this function is a list of strings, that are the rows
def arrange(forest):
    n = len(forest)
    forest = list(map(list, forest)) # make each element of foerst a list, then put that into a list again
    for i, f in enumerate(forest):
        forest[i] = [int(t) for t in f]
    grid = np.array(forest).reshape(n, -1) # reshape it to a 2D array of number of rows, and how many columns that it was!
    return grid

# Input of this function is a list of strings, before creating the grid
def treehouse(forest):
    grid = arrange(forest)
    r, c = grid.shape
    visibles = 2*((r-1)+(c-1)) # the outer trees are already visible
    scene_scores = []
    for i in range(1, r-1):
        for j in range(1, c-1):
            current = grid[i ,j]
            # for each tree, slice the map to its up, down, left, right
            up = grid[:i, j]
            down = grid[i+1:, j]
            left = grid[i, :j]
            right = grid[i, j+1:]
            directions = [up, down, left, right]
            
            # for part 1
            talls = [np.max(x) for x in directions] # the tallest tree in each direction
            
            # for part 2
            locs = [np.where(x >= current)[0] for x in directions] # trees that are taller than current, in each direction
            # we have numpy arrays in locs, that are either empty or they contain the indices of taller trees
            
            
            for l, loc in enumerate(locs):
                # the index for each direction -> and the closest we see for each direction
                # up: 0 -> max , down: 1 -> min, left: 2 -> max, right: 3 -> min
                if loc.size: # there are taller tree(s)
                    if l%2: # it's down or right
                        locs[l] = np.min(loc)+1 # we add this one because 
                    else: # it's up or left
                        locs[l] = np.max(loc)
                else: # it means that the current tree is the tallest
                    match l:
                        case 0: locs[l] = 0
                        case 1: locs[l] = r-1 -i
                        case 2: locs[l] = 0
                        case 3: locs[l] = c-1 -j
                            
            # viewing distance
            talls_loc = [i - locs[0], locs[1], j - locs[2], locs[3]]
            scene_scores.append(np.prod(talls_loc))
            
            # for part 1
            if current > min(talls):
                visibles += 1
    return visibles, max(scene_scores)

test_input = ["30373",
"25512",
"65332",
 "33549", 
 "35390"]

# print(f"number of total visible trees: {treehouse(test_input)}")
print(f"number of total visible trees: {treehouse(forest)}")
