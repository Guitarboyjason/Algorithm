from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
graph = [list(input()) for _ in range(n)]

# 벽을 뚫고 들어가는 횟수를 확인한다...
directions = [
    (i, j) for j in range(-1, 2) for i in range(-1, 2) if i != j and (i == 0 or j == 0)
]
# print(directions)
visited = [[3000 for _ in range(n)] for _ in range(n)]
visited[0][0] = 0
# root = [0,0]

queue = deque()
queue.append((0, 0, 0))  # x,y,cnt

while queue:
    x, y, cnt = queue.popleft()
    for nx, ny in directions:
        nx += x
        ny += y
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == "1" and visited[nx][ny] > cnt:
                visited[nx][ny] = cnt
                queue.append((nx, ny, cnt))
            elif graph[nx][ny] == "0" and visited[nx][ny] > cnt + 1:
                visited[nx][ny] = cnt + 1
                queue.append((nx, ny, cnt + 1))
print(visited[n - 1][n - 1])
