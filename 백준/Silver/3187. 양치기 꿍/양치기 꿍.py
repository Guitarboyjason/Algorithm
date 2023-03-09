# 양의 숫자가 늑대의 숫자보다 많을 경우 양
# 나머지 늑대
# 빈공간 : '.'
# 울타리 : '#'
# 늑대 : 'v'
# 양 : 'k'

# 무조건 늑대와 양은 울타리 안에 존재한다.

from collections import deque
import sys
input = sys.stdin.readline

cnt_w = 0
cnt_s = 0

R,C = map(int,input().split())
graph = list(input()for _ in range(R))
visited = list(list(False for _ in range(C))for _ in range(R))
def bfs(x,y):
    global cnt_w,cnt_s
    cnt_wolves = 0
    cnt_sheep = 0
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        if visited[x][y]:
            continue
        if graph[x][y] == 'v':
            cnt_wolves += 1
        if graph[x][y] == 'k':
            cnt_sheep+= 1
        visited[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= R or ny >= C:
                continue
            if visited[nx][ny]:
                continue
            if graph[nx][ny] == '#':
                continue
            else:
                queue.append((nx,ny))

    if cnt_wolves < cnt_sheep :
        cnt_s += cnt_sheep
    else:
        cnt_w += cnt_wolves

for i in range(R):
    for j in range(C):
        if not visited[i][j] and graph[i][j] != '#':
            bfs(i,j)

print(cnt_s,cnt_w)
