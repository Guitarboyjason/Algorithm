import sys
input = sys.stdin.readline
import enum


N = int(input())
arr = [0]*8003
for i in range(N):
    arr[int(input())+4001]+=1

sum = 0
count = 0
middle = 4001
tmp_list = list(index-4001 for index,i in enumerate(arr) if i != 0)
min_value,max_value = tmp_list[0],tmp_list[-1]
for index,i in enumerate(arr):
    if i != 0:
        sum += (index-4001) * i
        if count <= N // 2:
            count += i
            middle = index-4001
print(round(sum/N))# 산술평균
print(middle)#중앙값

if arr.count(max(arr)) != 1:
    print(list(index - 4001 for index,i in enumerate(arr) if i!= 0 and i == max(arr))[1])
else:
    print(arr.index(max(arr))-4001)

print(max_value-min_value)