from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit = 10**6


def DFS():
    stack = deque()
    stack.append(1)

    while stack:
        node = stack.pop()
        if visited[node] == False:
            visited[node] = True
            for i in nodes_relationships[node]:
                stack.append(i)
                if who_is_parent[i] == 0:
                    who_is_parent[i] = node


N = int(input())

node_line = [list(map(int, input().split()))for _ in range(N-1)]

nodes_relationships = [[]for _ in range(N+1)]
visited = [False for _ in range(N+1)]
who_is_parent = deque(0 for _ in range(N+1))

for i in node_line:
    nodes_relationships[i[0]].append(i[1])
    nodes_relationships[i[1]].append(i[0])
# print(nodes_relationships)
DFS()
who_is_parent.popleft()
who_is_parent.popleft()
for i in who_is_parent:
    print(i)
