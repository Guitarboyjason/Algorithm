
from collections import deque

n = int(input())

arr = [int(input()) for _ in range(n)]

stack = []
rlt = []
j = 0
for i in range(1, n+1):
    stack.append(i)
    rlt.append("+")

    while j < n and arr[j] == stack[-1]:
        stack.pop()
        rlt.append("-")
        j += 1
        if not stack:
            break

if stack:
    print("NO")
else:
    for char in rlt:
        print(char)

# 1 2 3 4
# 4 3
# 5 6
# 6
# 7 8
# 8 7 5 2 1
