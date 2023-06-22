"""
0인 구간은 0 나머지는 -1 로 ? 초기화 해 두고 최솟값으로 계속 업데이트 하면 될듯
"""
# dfs나 bfs로 구현하면 되겠다.
from collections import deque
import pprint

n, m = map(int, input().split())

direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]
graph = [list(map(int, input().split())) for _ in range(n)]

goal = [-1, -1]
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            goal = [i, j]
            break
    if goal != [-1, -1]:
        break


def bfs(graph, root):
    answer = [[-1 for _ in range(m)] for _ in range(n)]
    answer[root[0]][root[1]] = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                answer[i][j] = 0
    queue = deque()

    queue.append(root + [0])

    while queue:
        x, y, dist = queue.popleft()

        for i in range(4):
            nx, ny = direction[i]
            nx += x
            ny += y

            if 0 <= nx < n and 0 <= ny < m:
                if answer[nx][ny] == -1 or answer[nx][ny] > dist + 1:
                    answer[nx][ny] = dist + 1
                    queue.append((nx, ny, answer[nx][ny]))

    return answer


answer = bfs(graph, goal)
# pprint.pprint(answer)
for i in range(n):
    print(*answer[i])
