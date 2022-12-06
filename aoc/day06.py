with open("day06.txt", "rt") as input_file:
    buffer = input_file.read()

def start_of_packet(buffer):
    for i in range(len(buffer)):
        if i+4 >= len(buffer):
            return None
        if len(set(buffer[i:i+4])) == len(buffer[i:i+4]):
            return i+4

def start_of_message(buffer):
    for i in range(len(buffer)):
        if i < 14: continue
        if len(set(buffer[i-14:i])) == 14:
            return i
    return None





### tests
test_input1 = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
test_input2 = "bvwbjplbgvbhsrlpgdmjqwftvncz"
test_input3 = "nppdvjthqldpwncqszvftbrmjlhg"
test_input4 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
test_input5 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
test_input6 = "zcfzfwzzqfz"



def test_1():
    assert start_of_packet(test_input1) == 7
    assert start_of_message(test_input1) == 19

def test_2():
    assert start_of_packet(test_input2) == 5
    assert start_of_message(test_input2) == 23

def test_3():
    assert start_of_packet(test_input3) == 6
    assert start_of_message(test_input3) == 23

def test_4():
    assert start_of_packet(test_input4) == 10
    assert start_of_message(test_input4) == 29

def test_5():
    assert start_of_packet(test_input5) == 11
    assert start_of_message(test_input5) == 26

print("start_of_packet: ", start_of_packet(buffer))
print("start_of_message: ", start_of_message(buffer))