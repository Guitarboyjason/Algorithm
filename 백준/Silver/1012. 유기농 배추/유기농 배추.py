from collections import deque

def bfs(x,y):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M :
                if graph[nx][ny] == 1:
                    queue.append((nx,ny))
                    graph[nx][ny] = 0




for _ in range(int(input())):
    M,N,K = map(int,input().split())
    graph = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        y,x = map(int,input().split())
        graph[x][y] = 1

    cnt = 0
    for index_i,i in enumerate(graph):
        for index_j,j in enumerate(i):
            if j == 1:
                cnt += 1
                bfs(index_i,index_j)
    print(cnt)
