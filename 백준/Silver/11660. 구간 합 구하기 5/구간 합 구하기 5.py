from pprint import pprint

import sys
input = sys.stdin.readline

N,M = map(int,input().split())
'''
N <= 1024 이고, M <= 100_000 이므로
단순히 계산한다면 N**2 * M번은 말도 안되는 수

따라서 미리 저장해두면 좋을 것 같다.
어떻게?
x,y는
(x-1,y) + (x,y-1) - (x-1,y-1)
라고 했을 때, 문제점은 1,1에서출발하는게 아니라면 이다.

x1,y1에서 x2,y2까지는, 
(x2,y2) - (x1,y2) - (x2,y1) + (x2,y2)라고 볼 수 있을 것.
'''
graph = [[0 for _ in range(N+1)]]+[([0]+list(map(int,input().split())))for _ in range(N)]
# pprint(graph)
# dp = [[0 for _ in range(N)]for _ in range(N)]
for x in range(1,N+1):
    for y in range(1,N+1):
        # if x == 0 and y == 0:
        #     continue
        # if x == 0:
        #     graph[x][y] +=graph[x][y-1]
        # elif y == 0:
        #     graph[x][y] += graph[x-1][y]
        # else:
        graph[x][y] += graph[x-1][y] + graph[x][y-1] - graph[x-1][y-1]
# pprint(graph)
for _ in range(M):
    x1,y1,x2,y2 = map(int,input().split())
    print(graph[x2][y2] - graph[x1-1][y2] - graph[x2][y1-1] + graph[x1-1][y1-1])