import sys, heapq
input = sys.stdin.readline

arr = [0 for _ in range(10001)]
for _ in range(int(input())):
    arr[int(input())] += 1
for index,i in enumerate(arr):
    for j in range(i):
        print(index)
