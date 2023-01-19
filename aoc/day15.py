import re
from collections import Counter
import copy

# To read the input and turn it into a dict of sensor: manhattan distance covered by that sensor
# and to have the number of rows and columns
# input is the text of file_name
# output is a dictionary of locations of sensors and set of beacons
def read_input(file_name):
    sensors = dict()
    # because we can have location of a beacon multiple times
    beacons = set()
    with open(file_name, "rt") as my_input:
        for line in my_input:
            [xs, ys, xb, yb] = list(map(int, re.findall('[0-9]+', line)))
            beacons.add((xb, yb))
            delta = abs(xs-xb) + abs(ys-yb)
            sensors[(xs, ys)] = delta
    return sensors, beacons


# For the specific line, vertical or horizontal, we'll have intervals of coverage
# input is a dictionary of locations, as sensor:distance
# output is two dictionaries of intervals of coverage, for x-axis and y-axis, as line_number: [intervals]
def y_coverage(sensors, n):
    yintervals = []
    for sensor in sensors:
        xs, ys = sensor
        delta = sensors[sensor]
        # if the sensor covers the desired horizontal line
        if ys - delta <= n <= ys + delta:
            h = n - ys
            d = delta - abs(h)
            yintervals.append((xs- d, xs + d))
    return yintervals

def x_coverage(sensors, n):
    xintervals = []
    for sensor in sensors:
        xs, ys = sensor
        delta = sensors[sensor]
        # if the sensor covers the desired vertical line
        if xs - delta <= n <= xs + delta:
            h = n - xs
            d = delta - abs(h)
            xintervals.append((ys- d, ys + d))
    return xintervals


# This is to compare two intervals and return the merged if it's possible
# input is two intervals as tuples
# output is a list of interval in case of merge, or an empty list if no merge was possible
def merge_helper(int1, int2):
    a1, b1 = int1
    a2, b2 = int2
    start = min(a1, a2)
    end = max(b1, b2)
    # [a1,b1] , [a2,b2]
    if end == b2:
        if min(b1, a2) == a2:
            # this means we have overlap
            return [(start, end)]
    # same thing, in the other order
    if end == b1:
        if min(b2, a1) == a1:
            return [(start, end)]
    # no overlap:
    return []


# This is mergeing a bunch of intervals
# input is a list of tuples of intervals
# output is a list of tuple(s) of interval(s)
def merge(intervals):
    merged = copy.deepcopy(intervals)
    while True:
        for current in intervals:
            temp = copy.deepcopy(merged)
            while(temp):
                i = temp.pop()
                merge_out = merge_helper(current, i)
                if merge_out:
                    # if we merged two interval, but not to oneself, we need to remove the original intervals
                    if merge_out[0] != current and current in merged:
                        merged.remove(current)
                    if merge_out[0] != i and i in merged:
                        merged.remove(i)
                    # and add the new interval
                    if merge_out[0] != current and merge_out[0] != i and merge_out[0] not in merged:
                        merged.extend(merge_out)
        # we keep doing the merge until there is no more merge to do 
        if Counter(intervals) == Counter(merged):
            break
        # to merge the new intervals, that we got from merging the old ones
        intervals = copy.deepcopy(merged)
    return merged




# This is to compute the number of possible beacson locations
# input is x_intervals or y_intervals, dictionary of sensor:becaon locations, and the desired line to count as
# output is the number of possible positions for a beacon
def impossible_pos(intervals, bmap, n):
    count = 0
    for xb, yb in bmap:
        if yb == n:
            for ai, bi in intervals:
                if ai <= xb <= bi:
                    count -= 1
    for ai, bi in intervals:
        count += bi-ai+1
    return count


# for part 2:  
def possible_pos(sensors, beacons):
    for y in range(4000000):
        yintervals = y_coverage(sensors, y)
        ymerged = merge(yintervals)
        if len(ymerged) > 1: # means there is a gap
            # make sure that is not already a beacon:
            for i in range(len(ymerged)-1):
                a1, b1 = ymerged[i]
                a2, b2 = ymerged[i+1]
                if a2 > b1: a, b = a2, b1
                if a1 > b2: a, b = a1, b2
                # point between the gaps is the potential position
                d = a-b-1
                # there is only one possible position
                if d == 1:
                    # potential x
                    x = b+d
                    if (x,y) not in beacons:
                        # now we check the vertical intervals
                        xintervals = x_coverage(sensors, x)
                        xmerged = merge(xintervals)
                        if len(xmerged) > 1:
                            for j in range(len(xmerged)-1):
                                s1, e1 = xmerged[j]
                                s2, e2 = xmerged[j+1]
                                if s2 > e1: s, e = s2, e1
                                if s1 > e2: s, e = s1, e2
                                h = s-e-1
                                # again, there is only one possible position
                                if h == 1:
                                    # if the x in the gap: e+h is the potential x
                                    if e+h == y:
                                        return (x*4000000 + y)




def main():
    # y = 10
    # based on question
    y=2000000 

    # step 1: read and turn the input into a map of sensors
    # sensors, beacons = read_input("day15_test.txt")
    sensors, beacons = read_input("day15.txt")

    # step 2: compute the intervals based on map
    yintervals = y_coverage(sensors, y)

    # step 3: merge the intervals 
    merged = merge(yintervals)

    # step 4: count the possible beacon positions
    count = impossible_pos(merged, beacons, y)

    
    print(f"Part 1: {count}")
    print(f"Part 2: {possible_pos(sensors, beacons)}")

    return

main()
