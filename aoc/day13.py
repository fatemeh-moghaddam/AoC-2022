# to read the input and turn it into a list of tuple of signals that are to compare
def read_input(file_name):
    with open(file_name, "rt") as my_input:
        raw_signals = [line.strip() for line in my_input]
    flag = True
    signals = []
    for s in raw_signals:
        if s == '':
            signals.append((left, right))
            flag = True
            continue
        if flag:
            left = eval(s)
            flag = False
        else:
            right = eval(s)
    signals.append((left, right))
    return signals



def compare(left, right):
    if isinstance(left, list) or isinstance(right, list):
        if isinstance(left, list):
            if isinstance(right, list):
                for i in range(len(left)):
                    try:
                        comparison = compare(left[i], right[i])
                        if comparison == 0:
                            continue
                        else:
                            return comparison
                    except IndexError: # means that right was over before left
                        return -1
                # if we are here, we compared everything in left list, all items were the same
                # so now we compare based on length
                if len(left) == len(right):
                    return 0
                else:
                    return 1
            else: # then right is an integer, left is a list
                return compare(left, [right])
        else: # then left is an integer, right is a list
            return compare([left], right)
    # at this point both were integers
    elif left > right:
        return -1
    elif left < right:
        return 1
    else: # left == right
        return 0


## for part 1
def in_count(signals):
    in_order = 0
    new_signals = []
    for i, sigs in enumerate(signals):
        l, r = sigs
        res = compare(l, r)
        if res > 0:
            in_order += i+1
            new_signals.extend([l,r])
        else: # this is not necessary, just to use the comparison result here and make it faster later
            new_signals.extend([r,l])
    return in_order, new_signals


## for part 2
def insertion_sort(my_list):
    ssorted = [[[2]], [[6]]]
    while(my_list):
        item = my_list.pop(0)
        # traverse the sorted list backwards to stop at any point that item is bigger, because the list is sorted 
        for i in range(len(ssorted)-1, -1, -1):
            # right = item, left = ssorted[i]
            c = compare(ssorted[i], item)
            if c == 1:
                if i == len(ssorted)-1:
                    ssorted.append(item)
                else:
                    ssorted.insert(i+1, item)
                break
        if item not in ssorted:
            ssorted.insert(0, item)
    return ssorted




def main():
    # signals = read_input("day13_test.txt")
    signals = read_input("day13.txt")
    n , signals_list = in_count(signals)
    div1 = [[2]]
    div2 = [[6]]
    sorted_signals = insertion_sort(signals_list)
    print(f"Part 1: {n}")
    print(f"Part 2: {(sorted_signals.index(div1)+1) * (sorted_signals.index(div2)+1)}")


main()