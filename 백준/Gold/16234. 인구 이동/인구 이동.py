from collections import deque

def move_graph(graph):
    visited = [[False for _ in range(N)] for _ in range(N)]
    queue = deque()
    flag = False
    for i in range(N):
        for j in range(N):
            if visited[i][j] == False:
                root = (i,j)
                queue.append(root)
                visited[i][j] = True
                
                tmp_visited = []
                while queue:
                    # visited[root[0]][root[1]] = True
                    x,y = queue.popleft()
                    tmp_visited.append((x,y))
                    for nx,ny in directions:
                        nx += x
                        ny += y
                        if 0<=nx<N and 0<=ny<N and visited[nx][ny] == False and L<=abs(graph[x][y]-graph[nx][ny])<=R:
                            visited[nx][ny] = True
                            flag = True
                            queue.append((nx,ny))
                change_num = int(sum([graph[x][y] for x,y in tmp_visited]) / len(tmp_visited))
                for x,y in tmp_visited:
                    graph[x][y] = change_num
    if flag:
        return True
    else:
        return False
N,L,R = map(int,input().split())

graph = [list(map(int,input().split()))for _ in range(N)]

directions = [(i,j) for i in range(-1,2) for j in range(-1,2) if (i == 0 or j == 0) and i != j]

cnt = 0
while move_graph(graph):
    cnt += 1
print(cnt)