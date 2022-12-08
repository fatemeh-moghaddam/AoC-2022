import re

with open("day07.txt", "rt") as input_file:
    directions = [line.strip() for line in input_file]


class Folder:
    def __init__(self, name = "home"):
        self.name = name
        self.parent = None
        self.children = []
        self.size = 0

    def branch(self, name):
        new_folder = Folder(name)
        self.children.append(new_folder)
        new_folder.parent = self
        return new_folder
    
    def BFS(self):
        sizes = []
        queue = [self]
        while(queue):
            current = queue.pop(0)
            sizes.append(current.size)
            queue.extend(current.children)
        return sizes
        


def commands(cmd):
    cmd = cmd.strip("$ ")
    what = []
    if re.match("cd [a-z]+", cmd):
        child = cmd.split("cd ")[1]
        what.extend(["forward", child])
    if cmd == "cd ..":
        what.append("back")
    if cmd == "ls":
        pass
    return what
        

def count_size(logfile):
    current = Folder()
    parent = current
    output = 0
    for cmd in logfile:
        if "$" in cmd:
            what_to_do = commands(cmd)
            match len(what_to_do):
                case 0: # ls
                    continue
                case 1: # back
                    if current.size <= 100000: 
                        output += current.size
                        # add the size of current to size of parent
                    parent = current.parent
                    parent.size += current.size
                        # go to previous folder
                    current = parent
                case 2: # forward, child
                        # change current folder to child
                    child = what_to_do[1]
                    current = current.branch(child)
        elif "dir" in cmd: continue
        else: # add the size to current size
            [file_size] = list(map(int, re.findall('[0-9]+', cmd)))
            current.size += file_size

    current.parent.size += current.size
    current = current.parent

    available = 70000000 - current.size
    sizes = current.BFS()
    candidates = [s for s in sizes if s + available >= 30000000]

    return output, min(candidates)


        






test_input = ["$ cd /",
"$ ls",
"dir a",
 "14848514 b.txt", 
 "8504156 c.dat",
 "dir d",
 "$ cd a",
 "$ ls",
 "dir e",
 "29116 f",
 "2557 g",
 "62596 h.lst",
 "$ cd e",
 "$ ls",
 "584 i",
 "$ cd ..",
 "$ cd ..",
 "$ cd d",
 "$ ls",
 "4060174 j",
 "8033020 d.log",
 "5626152 d.ext",
 "7214296 k"]

print(f"the sum of the total sizes: {count_size(test_input)}")
print(f"the sum of the total sizes: {count_size(directions)}")

