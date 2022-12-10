import numpy as np

with open("day08.txt", "rt") as input_file:
    forest = [line.strip() for line in input_file]


def arrange(forest):
    n = len(forest)
    forest = list(map(list, forest))
    for i, f in enumerate(forest):
        forest[i] = [int(t) for t in f]
    grid = np.array(forest).reshape(n, -1)
    return grid

def treehouse(forest):
    grid = arrange(forest)
    r, c = grid.shape
    visibles = 2*((r-1)+(c-1))
    scene_scores = []
    for i in range(1, r-1):
        for j in range(1, c-1):
            current = grid[i ,j]
            up = grid[:i, j]
            down = grid[i+1:, j]
            left = grid[i, :j]
            right = grid[i, j+1:]
            directions = [up, down, left, right]

            talls = [np.max(x) for x in directions]
            
            locs = [np.where(x >= current)[0] for x in directions]
            
            for l, loc in enumerate(locs):
                    # up: 0 -> max , down: 1 -> min, left: 2 -> max, right: 3 -> min
                if loc.size:
                    if l%2: # it's down or left
                        locs[l] = np.min(loc)+1
                    else: # it's up or right
                        locs[l] = np.max(loc)
                else:
                    match l:
                        case 0: locs[l] = 0
                        case 1: locs[l] = r-1 -i
                        case 2: locs[l] = 0
                        case 3: locs[l] = c-1 -j

            talls_loc = [i - locs[0], locs[1], j - locs[2], locs[3]]
            scene_scores.append(np.prod(talls_loc))
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
