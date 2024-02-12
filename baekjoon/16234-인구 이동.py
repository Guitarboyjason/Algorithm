from collections import deque

directions = [(-1,0),(1,0),(0,-1),(0,1)]

def available_to_union(position1,position2):
    if L<=countries[position1[0]][position1[1]] - countries[position2[0]][position2[1]]<=R:
        return True
    return False

def check_to_union(pos):
    movable = []
    x,y = pos
    for nx,ny in range(directions):
        nx += x
        ny += y
        if 0<=nx<N and 0<=ny<N:
            if available_to_union((x,y),(nx,ny)):
                movable.append((nx,ny))
    return movable

def union_checker(pos):
    queue = deque([pos])
    visited = [[False for _ in range(N)]for _ in range(N)]
    summary = 0
    while queue:
        x,y = queue.popleft()
        if visited[x][y] == False:
            visited[x][y] = True
            summary += countries[x][y]
            union_list = [i for i in check_to_union((x,y)) if visited[i[0]][i[1]] == False]
            queue.extend(union_list)
    return visited, int(summary/sum([row.count(True) for row in visited]))


N,L,R = map(int,input().split())

countries = [list(map(int,input().split()))for _ in range(N)]

while True:
    done_flag = True
    visited = []
    for r in range(N):
        for c in range(N):
            if (r,c) not in visited:
                n_visited, next_int = union_checker((r,c))
                visited.extend(n_visited)
                for x,y in n_visited:
                # if countries[r][c] != next_int:
                #     done_flag = False
                #     for country
                    if countries[x][y] != next_int:
                        done_flag = False
                        countries[x][y] = next_int