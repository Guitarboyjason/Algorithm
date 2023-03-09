from collections import deque

M,N,H = map(int,input().split())

graph = [[list(map(int,input().split()))for _ in range(N)]for _ in range(H)]

def tomato(good_tomatos):
    dx = [0,0,0,0,1,-1]
    dy = [1,-1,0,0,0,0]
    dz = [0,0,1,-1,0,0]

    queue = good_tomatos

    while queue:
        x,y,z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0<=nx<H and 0<=ny<N and 0<=nz<M:
                if graph[nx][ny][nz] == 0:
                    graph[nx][ny][nz] = graph[x][y][z] + 1
                    queue.append((nx,ny,nz))
good_tomatos = deque()
for index_i, i in enumerate(graph):
    for index_j , j in enumerate(i):
        for index_k, k in enumerate(j):
            if k == 1:
                good_tomatos.append((index_i,index_j,index_k))
tomato(good_tomatos)
never = False
max_num = 0
for index_i, i in enumerate(graph):
    for index_j , j in enumerate(i):
        for index_k, k in enumerate(j):
            if k == 0:
                never = True
        if max(j) > max_num:
            max_num = max(j)

if never :
    print(-1)
else:
    print(max_num-1)
