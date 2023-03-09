import sys

input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
compare = arr[-1]

cnt = 1
for i in range(N-2,-1,-1):
    if arr[i] > compare:
        cnt += 1
        compare = arr[i]
print(cnt)