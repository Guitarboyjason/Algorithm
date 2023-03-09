from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit = 1000000000


def DFS(start_node):
    stack = deque()
    stack.append(start_node)

    while stack:
        node = stack.pop()
        if visited[node] == False:
            visited[node] = True
            if node in arr_node:
                for i in arr_node[node]:
                    stack.append(i)


N, M = map(int, input().split())

node_line = [list(map(int, input().split()))for _ in range(M)]
visited = [False]*(N+1)
arr_node = dict()

for i in node_line:
    if i[0] not in arr_node:
        arr_node[i[0]] = [i[1]]
    else:
        arr_node[i[0]].append(i[1])
    if i[1] not in arr_node:
        arr_node[i[1]] = [i[0]]
    else:
        arr_node[i[1]].append(i[0])

# print(arr_node)
# for i in arr_node:
#     i.sort()
cnt = 0
for i in range(1, N+1):
    # print(i)
    if visited[i] == False:
        DFS(i)
        cnt += 1
print(cnt)
