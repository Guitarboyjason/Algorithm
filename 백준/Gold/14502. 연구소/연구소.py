from itertools import combinations
from collections import deque
from copy import deepcopy
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
directions = [(i,j) for j in range(-1,2) for i in range(-1,2) if (i ==0 or j ==0) and i != j]

def wall(graph:list,pos0,pos1,pos2):
    tmp_graph = deepcopy(graph)
    for x,y in [pos0,pos1,pos2]:
        tmp_graph[x][y] = 1
    for x in range(N):
        for y in range(M):
            if tmp_graph[x][y] == 2:
                dfs_cal_safe_zone(tmp_graph,(x,y))
    sum_0 = 0
    for row in tmp_graph:
        sum_0 += row.count(0)
    return sum_0

def dfs_cal_safe_zone(graph,root):
    visited = [root]
    queue = deque([root])
    while queue:
        x,y = queue.popleft()
        graph[x][y] = 3
        for nx,ny in directions:
            nx += x
            ny += y
            if 0<=nx<N and 0<=ny<M and (nx,ny) not in visited and graph[nx][ny] == 0:
                queue.append((nx,ny))
                visited.append((nx,ny))

N,M = map(int,input().split())
graph = [list(map(int,input().split()))for _ in range(N)]

possible_list = combinations([i for i in range(N*M)],3)
max_count_0 = -1
for num_list in possible_list:
    n0 = num_list[0]//M
    m0 = num_list[0]%M
    n1 = num_list[1]//M
    m1 = num_list[1]%M
    n2 = num_list[2]//M
    m2 = num_list[2]%M
    if not (graph[n0][m0] + graph[n1][m1] + graph[n2][m2]): # 주어진 조건에 만족
        p_count_0 = wall(graph,(n0,m0),(n1,m1),(n2,m2))
        if p_count_0 > max_count_0:
            max_count_0 = p_count_0
print(max_count_0)