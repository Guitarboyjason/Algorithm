# # 전깃줄이 겹치지 않게 하기 위해서는 겹치는 두 전깃줄 중 하나를 없애는 방법

# N = int(input())
# graph = dict()
# # cross = dict()
# for _ in range(N):
#     line_to_a ,line_to_b = map(int,input().split())
#     graph[line_to_a] = line_to_b
# cross = {i : [] for i in graph}

# for index,i_key in graph:
#     for jndex,j_key in graph:
#         if index > jndex and 

# 가장 긴 증가수열을 구하면 되겠구나
import sys
input = sys.stdin.readline
N= int(input())
graph = [list(map(int,input().split()))for _ in range(N)]
graph.sort()
dp = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if graph[i][1] > graph[j][1] and dp[j] >= dp[i]:
            dp[i] = dp[j]+1
print(N-max(dp))