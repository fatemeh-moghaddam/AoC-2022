from collections import Counter

## Warm Up 1
### Counting duplicates
def count_dupes(my_str):
    cnt = Counter(my_str.lower())
    dupes = [i for i in cnt if cnt[i] > 1]
    return len(dupes)

# print(count_dupes('abBcdea'))


## Warm Up 2
### Multiplicative persistence

def mp(n):
    cnt = 0
    while n > 10:
        digits = list(str(n))
        temp = 1
        for i in digits:
            temp *= int(i)
        cnt += 1
        n = temp
    return cnt

def mp_II(n):
    largest_n = 0
    largest_mp = 0
    for i in range(n, 10, -1):
        if mp(i) > largest_mp: 
            largest_mp = mp(i)
            largest_n = i
    return largest_mp, largest_n

print(mp(9999))
print(mp_II(9999))

def test_999(): 
    assert mp(999) == 4



