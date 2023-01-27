
from math import inf


def read_input(file_name):
    coors = []
    with open(file_name, "rt")as my_file:
        for line in my_file:
            [x,y,z] = list(map(int, line.strip().split(",")))
            coors.append((x,y,z))
    return coors



def neighbours(loc):
    ns = []
    x,y,z = loc
    for i in range(-1,2):
        if i != 0:
            ns.append((x+i, y, z))
            ns.append((x, y+i, z))
            ns.append((x, y, z+i))
    return ns



def surface(coors):

    xmax, ymax, zmax = -inf, -inf, -inf
    xmin, ymin, zmin = inf, inf, inf

    for droplet in coors:
        neighbourhood = neighbours(droplet)
        x,y,z = droplet

        xmax = max(x, xmax)
        ymax = max(y, ymax)
        zmax = max(z, zmax)

        xmin = min(x, xmin)
        ymin = min(y, ymin)
        zmin = min(z, zmin)

    
    maxborder = (xmax, ymax, zmax)
    minborder = (xmin, ymin, zmin)
    # print(f"max: {maxborder}")
    # print(f"min: {minborder}")
    

    # it can only be this amount of air bubbles inside
    maxairway = xmax * ymax * zmax - len(coors)
    
    # to not calculate these every time for an air bubble
    trapped_air = set()
    free_air = set()

    def trapped(start):
        if start in trapped_air:
            return True
        if start in free_air:
            return False

        # This part is similar to graph connected component
        queue = [start]
        seen = set()
        while queue:
            current = queue.pop()
            seen.add(current)
            # if we reach the borders, or have more air bubbles that can be inside,
            # then it's not trapped
            for i in range(3):
                if not minborder[i] <= current[i] <= maxborder[i] or len(seen) > maxairway:
                    free_air.update(seen)
                    return False
            neighbourhood = neighbours(current)
            for ns in neighbourhood:
                if ns not in seen and ns not in coors: # we only want airs
                    queue.append(ns)
        trapped_air.update(seen)
        return True


    
    blocked_face = 0
    blocked_air = 0
    
    
    for drop in coors:
        neighbourhood = neighbours(drop)
        for ns in neighbourhood:
            if ns in coors: # if this face is faced to another block
                blocked_face += 1
            elif trapped(ns): # if it's air, but it doesn't have a way out
                blocked_air += 1

    area = len(coors)*6

    return area - blocked_face, area - blocked_face - blocked_air

def main():
    # coors  = read_input("day18_test.txt")
    coors  = read_input("day18.txt")
    total_area, external_area = surface(coors)
    print("Part 1: ", total_area)
    print("Part 2: ", external_area)
    return

main()


