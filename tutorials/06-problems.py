### 1
def read_file():
    with open("06-numbers.txt", "rt") as myfile:
        numbers = myfile.read().split()
    return numbers

## 1_1
def sorted_mod_7_1(numbers): 
    return sorted(numbers, key = mod_7, reverse = True)

def mod_7(n):
    return n % 7

## 1_2
def sorted_mod_7_2(numbers): 
    return sorted(numbers, key = lambda n: n % 7, reverse = True)

# (lambda num_list: num_list.sort(key = lambda n: n % 7, reverse = True))
print(sorted_mod_7_2([5, 48, 98]))

## tests
def test_mode7():
    assert sorted_mod_7_1([5, 48, 98]) == [48, 5, 98]
    assert sorted_mod_7_2([5, 48, 98]) == [48, 5, 98]
