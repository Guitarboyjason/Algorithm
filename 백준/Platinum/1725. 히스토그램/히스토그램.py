
import sys
input = sys.stdin.readline
N = int(input())
histogram = [int(input()) for _ in range(N)] + [0]
max_size = 0
c = 0
stack = []

for i in range(N+1):
    c = i
    while stack and stack[-1][0] >= histogram[i]:
        h, plus_c = stack.pop()
        # size.append(h * (i-plus_c))
        if h * (i-plus_c) > max_size:
            max_size = h * (i-plus_c)
        c = plus_c

    stack.append([histogram[i], c])

print(max_size)

