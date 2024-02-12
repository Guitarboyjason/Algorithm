# 이차원을 그려서 0: 친구 x, 1: 친구 , 2: 2친구

import sys
from pprint import pprint

input = sys.stdin.readline
N = int(input())
graph = [list(input().rstrip()) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if (
                (k != i and k != j and i != j)
                and graph[i][j] == "N"
                and graph[i][k] == "Y"
                and graph[k][j] == "Y"
            ):
                graph[i][j] = 2

# pprint(graph)
print(N - min([row.count("N") for row in graph]))
