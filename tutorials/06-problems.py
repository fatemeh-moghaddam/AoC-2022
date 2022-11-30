
######## 1. Lambda expressions
## 1_a_1
def sorted_mod_7_1(numbers): 
    return sorted(numbers, key = mod_7, reverse = True)

def mod_7(n):
    return n % 7

## 1_a_2
def sorted_mod_7_2(numbers): 
    return sorted(numbers, key = lambda n: n % 7, reverse = True)

## tests
def test_mode7():
    assert sorted_mod_7_1([5, 48, 98]) == [48, 5, 98]    
    ## 1_b
def test_lambda():
    assert [48, 5, 98] == (lambda num_list: sorted(num_list, key = lambda n: n % 7, reverse = True))([5, 48, 98])

######## 2. Using map vs. list comprehension
### 1. Read the file numbers.txt (all in one line, space-separated).

with open("06-numbers.txt", "rt") as myfile:
    nums_str = myfile.read().split()

### 2.a Convert the list of strings to a list of numbers using map
def convert_2_a(nums):
    return list(map(int, nums))

### 2.b Convert the list of strings to a list of numbers using a list comprehension
def convert_2_b(nums):
    return [int(n) for n in nums]

### 3.a For each element get the the next larger number that is a square, using map
from math import sqrt
def next_sqr_a(nums):
    return list(map(lambda n: (int(sqrt(int(n)))+1)**2, nums))


### 3.b For each element get the the next larger number that is a square, using list comprehension
def next_sqr_b(nums):
    return [(int(sqrt(int(n)))+1)**2 for n in nums]


### 4. check
def test_2():
    assert convert_2_a(nums_str) == convert_2_b(nums_str)
def test_3():
    assert next_sqr_a(nums_str) == next_sqr_b(nums_str)
def test_sum():
    assert sum(next_sqr_a(nums_str)) == 4990535095484285