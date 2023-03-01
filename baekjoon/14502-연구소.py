from collections import deque
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def bfs(graph, start):
    visited = []
    queue = deque()
    queue.append(start)
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            for x, y in direction:
                nx, ny = node[0]+x, node[1]+y
                if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
                    if graph[nx][ny] == 0 and [nx, ny] not in visited:
                        queue.append([nx, ny])
                        graph[nx][ny] = 2
    return graph


def count_bfs(graph):
    for i in range(len(graph)):
        tmp_graph = [i for i in graph]
        for j in range(len(graph[0])):
            if tmp_graph[i][j] == 2:
                tmp_graph = bfs(graph, [i, j])
    cnt = 0
    for i in graph:
        cnt += i.count("0")
    return cnt


N, M = map(int, input().split())
# N과 M이 크지 않아서 단순 브루트 포스로도 해결이 가능 할 것.
graph = ["".join(input().split())for _ in range(N)]
max_cnt = 0
print(graph)
for i in range(N):
    tmp_graph = [i for i in graph]
    for j in range(M):
        if tmp_graph[i][j] == "0":
            tmp_graph[i] = tmp_graph[i][:j] + "1" + tmp_graph[i][j+1:]
            for k in range(M):
                if tmp_graph[i][k] == "2":
                    cnt = count_bfs(graph)
                    if max_cnt < cnt:
                        max_cnt = cnt
print(graph)
print(max_cnt)
