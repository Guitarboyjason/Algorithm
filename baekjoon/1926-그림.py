
from collections import deque
direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def bfs(graph, node):
    queue = deque()
    queue.append(node)
    cnt = 0
    column_max = len(graph[0])
    row_max = len(graph)

    # print(queue)
    while queue:
        x, y = queue.popleft()
        if visited[x][y] == False:
            cnt += 1
            visited[x][y] = True
        # print(queue)
            for i in direction:
                nx = x+i[0]
                ny = y+i[1]
                if 0 <= nx < row_max and 0 <= ny < column_max and graph[nx][ny] == 1 and visited[nx][ny] == False:
                    # print(nx, ny)
                    queue.append([nx, ny])
                    # print(queue)
    # print(visited)
    # print(cnt)
    return cnt


n, m = map(int, input().split())
visited = list([False for _ in range(m)] for _ in range(n))
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
# print(graph)

cnt_list = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == False:
            cnt_list.append(bfs(graph, [i, j]))
# print(cnt_list)
if cnt_list:
    print(len(cnt_list), max(cnt_list))
else:
    print(0, 0)
