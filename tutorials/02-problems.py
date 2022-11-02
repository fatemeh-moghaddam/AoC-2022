import math
def my_max(my_list):
    maxi = -math.inf
    for element in my_list:
        if element > maxi:
            maxi = element
    return maxi

def process_list(my_list):
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            my_list[i] //= 2
        else:
            my_list[i] *= 2
        if i % 7 == 0:
            my_list[i] += i
    return my_max(my_list)


def collatz(my_int):
    temp = []
    while my_int not in temp:
        temp.append(my_int)
        if my_int % 2 == 0:
            my_int //= 2
        else:
            my_int = my_int*3 + 1
    print(temp)
    return temp[-1]

def compute_pi(my_int):
    pi = 0
    for i in range(my_int):
        pi += (-1)**i / (i*2 + 1)
    pi *= 4
    return pi

def integer_cube_root(n):
    for k in range(n):
        if k**3 >= n:
            break
    return k

def caesar(my_str):
    temp = ''
    for c in my_str:
        if c.isspace(): 
            temp += ' '
            continue
        if c == 'X':
            temp += my_str.replace(c, 'A')
        elif c == 'Y':
            temp += my_str.replace(c, 'B')
        elif c == 'Z':
            temp += my_str.replace(c, 'C')
        else:
            temp += chr(ord(c)+3)
    return temp

def caesar_2(my_str):
    temp = ''
    for c in my_str:
        if c.isspace(): 
            temp += ' '
            continue
        asc = ord(c) + 3
        if asc // (ord('Z')+1) != 0:
            asc = ord('A') + (asc % (ord('Z')+1))
        temp += chr(asc)
    return temp

# test = [1, -2, -5, -8 , -9]
test = list(range(8))
# print(integer_cube_root(28))
print(caesar("HELLO WORLD"))
