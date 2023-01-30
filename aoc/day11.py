import re

ops = {'+': lambda x, y: x+y,
       '*': lambda x, y: x*y}


class monkey:
    def __init__(self, num):
        self.num = num
        self.items = []
        self.tm = None      # If test == true, throuw to which monkey 
        self.fm = None      # If test == false, throuw to which monkey
        self.op = None      # If test == true, throuw to which monkey
        self.op_value = None    # value that the operation is done by
        self.tv = None          # value that the test is done by


# The input is the file name as a string
# The output is a dictionary that the keys are the monkey numbers and the values
# are the pointers to a class of monkey
def input_read(file_name):
    monkeys = dict()
    with open(file_name, "rt") as input_file:
        for line in input_file:
            if "Monkey" in line: # create a new monkey
                [num] = list(map(int, re.findall('[0-9]', line)))
                current = monkey(num)       
                monkeys[num] = current      
            # after here, it means that we already have a monkey called current
            if "Starting" in line:
                items = list(map(int, re.findall('[0-9]+', line)))
                current.items.extend(items)
            if "Operation" in line:
                op_params = line.split()
                value = op_params[-1]
                operation = op_params[-2]
                current.op = ops[operation]
                if value != "old":
                    current.op_value = int(value)
                else: # save the word "old" itself to figure later
                    current.op_value = value
            if "Test" in line:
                [tvalue] = list(map(int, re.findall('[0-9]+', line)))
                current.tv = tvalue
            if "true" in line:
                [tmonkey] = list(map(int, re.findall('[0-9]+', line)))
                current.tm = tmonkey
            if "false" in line:
                [fmonkey] = list(map(int, re.findall('[0-9]+', line)))
                current.fm = fmonkey
    return monkeys


# Input is the dictionary of monkeys, monkey_number : pointer to the monkey
def keep_away(monkeys):
    mon_count = [0 for _ in range(len(monkeys))]
    for _ in range(20):
        for id in monkeys:
            mon = monkeys[id]
            while mon.items:    # they empty all the items in their turn
                # count the number of items each monkey inspects
                mon_count[id] += 1
                # grab a new item in a queue manner
                wval = mon.items.pop(0)
                # Operation
                if mon.op_value == "old":
                    wval = mon.op(wval, wval)
                else:
                    wval = mon.op(wval, mon.op_value)
                # Relief
                wval //= 3
                if wval % mon.tv == 0:
                    new_mon_num = mon.tm
                else: 
                    new_mon_num = mon.fm
                new_mon = monkeys[new_mon_num]
                new_mon.items.append(wval)
    sorted_mons = sorted(mon_count, reverse= True)
    return sorted_mons[0] * sorted_mons[1]



def forever(monkeys):
    # This is to avoid for the worry value to get too large
    div = 1
    # because we are using % for the test, after the number is larger than the product of all test values,
    # we can get the mod of the worry_level % the product number
    for i in monkeys:
        div *= monkeys[i].tv
    mon_count = [0 for _ in range(len(monkeys))]
    for i in range(10000):
        for id in monkeys:
            mon = monkeys[id]
            while mon.items:
                # count the number of items each monkey inspects
                mon_count[id] += 1
                # grab a new item in a queue manner
                wval = mon.items.pop(0)
                # Operation
                if mon.op_value == "old":
                    wval = mon.op(wval, wval)
                else:
                    wval = mon.op(wval, mon.op_value)
                if wval % mon.tv == 0:
                    new_mon_num = mon.tm
                else: 
                    new_mon_num = mon.fm
                new_mon = monkeys[new_mon_num]
                new_mon.items.append(wval % div)
    sorted_mons = sorted(mon_count, reverse= True)
    return sorted_mons[0] * sorted_mons[1]
    # return mon_count


my_monkeys = input_read("day11.txt")
# my_monkeys = input_read("day11_test.txt")
print("Part 1: ", keep_away(my_monkeys))

my_monkeys = input_read("day11.txt")
# my_monkeys = input_read("day11_test.txt")
print("Part 2: ", forever(my_monkeys))


