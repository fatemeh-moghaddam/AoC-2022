from collections import defaultdict
import math

with open("day12.txt", "rt") as my_input:
    area = [line.strip() for line in my_input]



def neighborhood(i,j,r,c):
    ns = []
    if i != 0:
        ns.append((i-1,j))
    if i < r-1:
        ns.append((i+1,j))
    if j != 0:
        ns.append((i, j-1))
    if j < c-1:
        ns.append((i,j+1))
    return ns


def graphing(area):
    r = len(area)
    c = len(area[0])
    graph = defaultdict(list)
    start_cands = []
    for i in range(r):
        for j in range(c):
            current = area[i][j]
            neighbours = neighborhood(i,j,r,c)
            if current == 'a':
                start_cands.append((i,j))
            if current == 'S':
                start = (i,j)
                current = 'a'
                start_cands.append(start)
            if current == 'E':
                end = (i,j)
                continue
            for ns in neighbours:
                h,v = ns
                next = area[h][v]
                if next == 'E': next = 'z'
                delta = ord(next) - ord(current)
                if delta < 2:
                    graph[(i,j)].append((h,v))
            
    return start_cands, start, end, graph


# I used the uniform-cost search algorithm from AI course for this part
def hill_climbing(hill, start, end):
    explored = set()
    cost = 0
    frontier = {start:cost}
    while frontier:
        # this is replacing a priority queue ordered by ascending cost
        node = min(frontier, key = frontier.get)
        if node == end:
            return frontier[end]
        cost = frontier[node]
        frontier.pop(node)
        explored.add(node)
        for ns in hill[node]:
            new_node = ns
            if new_node not in explored and new_node not in frontier:
                frontier[new_node] = cost+1
            elif new_node in frontier:
                if frontier[new_node] > cost+1:
                    frontier[new_node] = cost+1
    # in case there was no way from that start to the end
    return math.inf


def trail(hill, starts, end):
    opt = math.inf
    for cor in starts:
        opt = min(opt, hill_climbing(hill, cor, end))
    return opt

        


def hiking(area):
    start_cands, start, end, grid = graphing(area)
    print("Part 1: ", hill_climbing(grid, start, end))
    print("Part 2: ", trail(grid, start_cands, end))
    return

test_input = ["Sabqponm", "abcryxxl", "accszExk", "acctuvwj", "abdefghi"]


# hiking(test_input)
hiking(area)

