import math
from itertools import permutations

def erathos(n):
    arr = {i:i for i in range(2,n+1)}
    for i in range(2,int(math.sqrt(n))+2):
        if i in arr:
            tmp = n // i
            for j in range(2,tmp+2):
                if i*j in arr:
                    # arr.popitem(tmp*j)
                    arr.pop(i*j)
    return arr.values()
# print(list(erathos(9999999)))
# print({i:i for i in range(2,100)})


def solution(numbers):
    
    return 

numbers = "17"
primenums = erathos(10**(len(numbers)))
nums_arr = ["1","2","3","4","5","6","7","8","9","0"]
perm_arr = []
tmp = ""
for i in range(1,len(numbers)+1):
    # print(list(permutations(numbers,i)))
    # for j in str(list(permutations(numbers,i))):
    #     print(j,end="")
    sign = 0
    
    for j in str(set(permutations(numbers,i))):
        if j == "(":
            sign = 1
            continue
        if j == ")":
            sign = 0
            perm_arr.append(tmp)
            tmp = ""
            continue
        if sign == 1 and j in nums_arr:
            tmp += j
perm_arr = set(map(int,perm_arr))

print(perm_arr)
count = 0
for i in perm_arr:
    if int(i) in primenums:
        count += 1
print(count)