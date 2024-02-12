import sys
input = sys.stdin.readline

N = int(input())

arr = [list(map(int,input().split()))for _ in range(N)]
arr.sort(key=lambda x:x[0])
arr.sort(key=lambda x:x[1])

last = 0
count = 0
for i,j in arr:
    if i >= last:
        count += 1
        last = j
print(count)


