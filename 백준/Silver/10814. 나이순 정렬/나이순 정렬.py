#10814-나이순정렬.py

import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    arr.append(input().split())

arr.sort(key=lambda x : int(x[0]))

for i in arr:
    print(i[0],i[1])