
from collections import deque


def DFS(start_node):
    visited = [0 for _ in range(N)]
    stack = deque()
    stack.append(start_node)
    while stack:
        node = stack.pop()
        for i in range(N):
            if arr[node][i] == 1 and visited[i] != 1:
                visited[i] = 1
                stack.append(i)
    return visited


N = int(input())
arr = [list(map(int, input().split()))for _ in range(N)]

for i in range(N):
    for i in DFS(i):
        print(i, end=" ")
    print()
