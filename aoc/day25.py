
with open("day25.txt", "rt")as my_file:
    numbers = [line.strip() for line in my_file]


SNAFU_ref = {'2':2, '1':1, '0':0, '-':-1, '=': -2}
deci_ref = {value:key for key, value in SNAFU_ref.items()}

# The input is a list of SNAFU numbers
def SNAFU_to_deci(snafu):
    # first step, to deicmal and sum
    output = 0
    for num in snafu:
        l = len(num)-1  # because it's from right to left, I need this for the power
        # I can just use the output to sum, but I wanted to check the numbers first
        decimal = 0
        for i, n in enumerate(num):
            decimal += SNAFU_ref[n] * 5**(l-i)
        output += decimal
    return output


# The input is a single decimal number
def deci_to_SNAFU(number):
    c = number % 5
    q = number // 5
    output = ''
    # we take care of q at last
    while q > 5 or c > 2:
        c = number % 5
        q = number // 5
        if c > 2:
            q += 1
            c = number - q*5
        output += deci_ref[c]
        number = q
    # because we don't have 3 and 4
    if q > 2:
        q = q - 5
        output += deci_ref[q]
        output += '1'
    else:
        output += deci_ref[q]
    # it's from right to left
    output = output[::-1]
    return output


test_input = ["1=-0-2",
"12111",
"2=0=",
"21",
"2=01",
"111",
"20012",
"112",
"1=-1=",
"1-12",
"12",
"1=",
"122"]


# print(deci_to_SNAFU(SNAFU_to_deci(test_input)))
print(deci_to_SNAFU(SNAFU_to_deci(numbers)))

"""""""""""""""""""""""""""""""""""""""""""""""
SNAFU  Decimal
1=-0-2     1747
 12111      906
  2=0=      198
    21       11
  2=01      201
   111       31
 20012     1257
   112       32
 1=-1=      353
  1-12      107
    12        7
    1=        3
   122       37 
"""""""""""""""""""""""""""""""""""""""""""""""
