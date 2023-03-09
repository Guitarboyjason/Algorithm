# 익 근처 익
# 토마토가 없는 경우도 있음
# 모두 익을 때 까지의 최소 날짜
# 처음부터 다 익어있으면 0
# 절대 익지 못하는 경우 -1

# 1 인 인덱스를 리스트로 받자
from collections import deque

M,N = map(int,input().split())
tomatos = [list(map(int,input().split()))for _ in range(N)]
max_days = 0
def bfs(list_1):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    queue = deque()
    for i in list_1:
        queue.append(i)
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if tomatos[nx][ny] == -1:
                continue
            if tomatos[nx][ny] == 0:
                tomatos[nx][ny] = tomatos[x][y] + 1
                queue.append((nx,ny))
summary_1 = 0
summary_0 = 0
list_1 = []
for i in tomatos:
    summary_1 += i.count(1)
    summary_0 += i.count(0)
if summary_1 == 0:
    print(-1)
elif summary_0 == 0:
    print(0)
else:
    been_broken = False
    for index_i,i in enumerate(tomatos):
        for index_j,j in enumerate(i):
            if j == 1:
                list_1.append((index_i,index_j))
    bfs(list_1)
    for i in tomatos:
        if 0 in i:
            been_broken = True
            break
        else:
            if max_days < max(i):
                max_days = max(i)

    if not been_broken:
        print(max_days-1)
    else:
        print(-1)
