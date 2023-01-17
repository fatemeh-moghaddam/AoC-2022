import re
from collections import Counter
import copy

# To read the input and turn it into a dict of sensor: beacon
# and to have the number of rows and columns
# input is the text of file_name
# output is a dictionary of locations of sensors and beacons
def read_input(file_name):
    sensors = dict()
    # because we can have location of a beacon multiple times
    beacons = set()
    with open(file_name, "rt") as my_input:
        for line in my_input:
            [xs, ys, xb, yb] = list(map(int, re.findall('[0-9]+', line)))
            sensors[(xs, ys)] = (xb, yb)
            beacons.add((xb, yb))
    return sensors, beacons


# For the specific line, vertical or horizontal, we'll have intervals of coverage
# input is a dictionary of locations, as sensor:beacon
# output is two dictionaries of intervals of coverage, for x-axis and y-axis, as line_number: [intervals]
def y_coverage(map, n):
    yintervals = []
    for sensor in map:
        xs, ys = sensor
        xb, yb = map[sensor]
        # manhattan distance
        delta = abs(xs-xb) + abs(ys-yb)
        # if the sensor covers the desired horizontal line
        if n >= ys - delta and n <= ys + delta:
            h = n - ys
            d = delta - abs(h)
            yintervals.append((xs- d, xs + d))
    return yintervals

def x_coverage(map, n):
    xintervals = []
    for sensor in map:
        xs, ys = sensor
        xb, yb = map[sensor]
        # manhattan distance
        delta = abs(xs-xb) + abs(ys-yb)
        # if the sensor covers the desired vertical line
        if n >= xs - delta and n <= xs + delta:
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
    # print(f"{merged=}")
    return merged


# This is to compute the number of possible beacson locations
# input is x_intervals or y_intervals, dictionary of sensor:becaon locations, and the desired line to count as
# output is the number of possible positions for a beacon
def possible_pos(intervals, map, n):
    count = 0
    for beacon in map:
        xb, yb = beacon
        if yb == n:
            for intr in intervals:
                ai, bi = intr
                if xb >= ai and xb <= bi:
                    count -= 1
    for intr in intervals:
        ai, bi = intr
        count += bi-ai+1
    return count


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
    count = possible_pos(merged, beacons, y)

    print(f"Part 1: {count}")

    return

main()
