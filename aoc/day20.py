
def read_input(file_name):
    with open(file_name, "rt") as my_file:
	    coors = [int(line.strip()) for line in my_file]
    return coors

class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None
        self.prev = None

class DLL:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


    def append(self, value):
        new_node = Node(value)

        #  --B--A   ->   --B--A--C
        # connect A to C
        self.tail.next = new_node
        # connect C to A
        new_node.prev = self.tail
        # now we can change the tail
        self.tail = new_node

        # because it's circular
        new_node.next = self.head
        self.head.prev = new_node

        self.length += 1
        return new_node


    # These two where not necessary, just to help me debug
    # helper
    def get_by_val(self, val):
        current = self.head
        i = 0
        while current.value != val:
            if i > self.length:
                return None
            current = current.next
            i += 1
        return current, i

    def get_by_index(self, index):
        if index < self.length/2:
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self.length-1, index, -1):
                current = current.prev  
        return current

    

    def get_by_order(self, start, n):
        current = start
        for i in range(n):
            current = current.next
        return current



    # helper
    def print_dll(self):
        current = self.head
        for _ in range(self.length):
            print(current.value)
            current = current.next
        return


    def insert_after(self, where, node):

        if where == self.tail: # means we are adding a in the tail's place
            self.tail = node
        # --A--B--  --C-- ->insert C after A->  --A--C--B--

        node.prev.next = node.next
        node.next.prev = node.prev

        node.prev = where
        node.next = where.next
        where.next.prev = node
        where.next = node
        
        return

    def insert_before(self, where, node):

        if where == self.head: # means we are adding a in the head's place
            self.head = node
        # --A--B--  --C-- ->insert C before B->  --A--C--B--

        node.prev.next = node.next
        node.next.prev = node.prev

        node.next = where
        node.prev = where.prev
        where.prev.next = node
        where.prev = node
        
        return



def mixing(coors):

    n = len(coors)

    # create the doubly linked list
    codes_dll = DLL(coors[0])
    # to go based on the original order
    nodes = [codes_dll.head]
    for i in range(1, n):
        new_node = codes_dll.append(coors[i])
        nodes.append(new_node)
    

    # only for part 2
    coors = [num* 811589153 for num in coors]

    def mixer(codes_dll):
        for num, node in zip(coors, nodes):
            # zero node won't change
            if num == 0:
                zero = node
                continue
            iter = abs(num) % (n-1)
            current = node
            for _ in range(iter):
                if num > 0:
                    current = current.next
                if num < 0:
                    current = current.prev
            if num > 0:
                codes_dll.insert_after(current, node)
            if num < 0:
                codes_dll.insert_before(current, node)
        return zero


    # Part 1
    # zero = mixer(codes_dll)

    # Part 2
    for _ in range(10):
        zero = mixer(codes_dll)


    # x = codes_dll.get_by_order(zero, 1000)
    # y = codes_dll.get_by_order(x, 1000)
    # z = codes_dll.get_by_order(y, 1000)
    # print("Part 1: ", x.value + y.value + z.value)

    # better written:
    output = 0
    for _ in range(3):
        for _ in range(1000):
            zero = zero.next
        output += zero.value

    
    # print("Part 1: ", output)
    print("Part 2: ", output*811589153)


    return codes_dll

def main():
    coors = read_input("day20.txt")
    # coors = [1, 2, -3, 3, -2, 0, 4]
    decoded = mixing(coors)
    return

main()

	

		