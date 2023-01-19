from collections import deque
import math

def convert_iter(num, base):
    power = 0
    tmp = ''
    while num:
        tmp = str(num%base) + tmp
        num //= base
    return tmp

def teneth(n):
    arr = deque([i for i in range(2,int(math.sqrt(n)+1))])
    tmp_arr = []
    while(arr):
        tmp = arr.popleft()
        tmp_arr.append(tmp)
        count = n // tmp
        for j in range(2,count+1):
            if tmp * j in arr:
                arr.remove(tmp*j)
        
    return tmp_arr

n = 885733
k = 3

word = convert_iter(n,k)
primenums = teneth(int(word))
words = word.split("0")
count = 0
print(words)
for i in words:
    if i != '' and int(i) in primenums:
        count += 1
print(count)