
from collections import deque
N = int(input())
trees_time_length = list(map(int, input().split()))
trees_time_length.sort()
time_for_invite = 0
day = N
while trees_time_length:
    day -= 1
    tree = trees_time_length.pop()
    if day + time_for_invite < tree:
        time_for_invite += tree-day - time_for_invite
    # print(tree, time_for_invite)

print(time_for_invite + N + 1)
