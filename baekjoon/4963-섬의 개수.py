from collections import deque
import sys
input = sys.stdin.readline

directions = [[i,j]for j in range(-1,2) for i in range(-1,2) if i!=0 or j != 0]
print(directions)

def count_islands(graph:list,root,w,h):  # 처음 찾은 1을 root에 넣을까 x
    # cnt = 0
    # while sum(sum(i) for i in graph):
        # cnt += 1
        # row_index = -1
        # column_index = -1
        # for row_idx, row in enumerate(graph):
        #     if 1 in row:
        #         row_index = row_idx
        #         column_index = row.index(1)
        #         break
        # if column_index == -1: # 들어올수가 없다
    # row_index = -1
    # column_index = -1
    # for i in range(w):
    #     for j in range(h):
    #         if graph[i][j] == 1:
    #             row_index = i
    #             column_index = j
    #             break
    #     if column_index:
    #         break
        
        # visited.append((row_index,column_index))
    queue = deque()
    queue.append(root)
    while queue:
        x,y = queue.popleft()
        # visited[x][y] = 1
        graph[x][y] = 0 # 0으로 바꿔준다.
        for nx,ny in directions:
            nx += x
            ny += y
            if 0<=nx<h and 0<=ny<w and graph[nx][ny] == 1:
                queue.append((nx,ny))
    # return cnt

w,h = map(int,input().split())

while w != 0 or h != 0:
    # print(visited)
    islands = [list(map(int,input().split()))for _ in range(h)]
    
    # print(count_islands(islands,w,h,visited))
    cnt = 0
    for i in range(h):
        for j in range(w):
            if islands[i][j] == 1:
                cnt += 1
                count_islands(islands,(i,j),w,h)
    print(cnt)
    w,h = map(int,input().split())