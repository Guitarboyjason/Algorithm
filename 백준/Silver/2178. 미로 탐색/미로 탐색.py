from collections import deque

N,M = map(int,input().split())
maze = [list(map(int,input()))for _ in range(N)]
graph = []
def find_min_route(x,y):
    dx = [-1,0,0,1]
    dy = [0,-1,1,0]
    stack = deque()
    stack.append((x,y))
    while stack:
        x,y = stack.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or ny < 0 or nx>=N or ny >=M:
                continue
            if maze[nx][ny] == 0 :
                continue
            if maze[nx][ny] == 1:
                stack.append([nx,ny])
                maze[nx][ny] = maze[x][y] + 1

    return maze[N-1][M-1]
print(find_min_route(0,0))


