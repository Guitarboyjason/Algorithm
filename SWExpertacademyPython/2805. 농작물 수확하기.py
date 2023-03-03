from collections import deque
import sys
sys.stdin = open("sources/input-11.txt", "r")


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    farm = deque()
    for _ in range(N):
        farm.append(input().split())
    half = N//2
    summary = 0
    for i in range(half):
        for j in range(half-i, half+i+1):
            summary += int(farm[0][0][j])
        farm.popleft()
    for i in range(N):
        summary += int(farm[0][0][i])
    farm.popleft()
    farm.reverse()
    for i in range(half):
        for j in range(half-i, half+i+1):
            summary += int(farm[0][0][j])
        farm.popleft()
    # print(summary)
    print("#{} {}".format(test_case, summary))
