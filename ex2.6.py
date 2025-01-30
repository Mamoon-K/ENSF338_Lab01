import timeit

def pow2(n):
    return 2 ** n

# Initial timeit section
# 10,000 tests of pow2(10000)
time1 = timeit.timeit("pow2(10000)", setup="from __main__ import pow2", number=10000)
print("Time to execute pow2(10000) 10,000 times: " + str(time1/10000))

# Timing of using for loops and list comprehension for 2^n for n from 1-1000
def pow2n_for():
    pow2nForList = []
    for n in range(1001):
        pow2nForList.append(2 ** n)
    return pow2nForList

def pow2n_list_comp():
    pow2nListComp = [2 ** n for n in range(1001)]
    return pow2nListComp

time2 = timeit.timeit("pow2n_for()", setup="from __main__ import pow2n_for", number=1000)
time3 = timeit.timeit("pow2n_list_comp()", setup="from __main__ import pow2n_list_comp", number=1000)
print("Time to execute pow2(n) for n from 1-1000, 1000 times with a for loop: " + str(time2/1000))
print("Time to execute pow2(n) for n from 1-1000, 1000 times with list comprehension: " + str(time3/1000))