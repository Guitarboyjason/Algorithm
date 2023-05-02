import sys
input = sys.stdin.readline
N= int(input())
graph = [list(map(int,input().split()))for _ in range(N)]
graph.sort()
dp = [1 for i in range(N)]

for i in range(N):
    for j in range(i):
        if graph[i][1] > graph[j][1] and dp[j] >= dp[i]:
            dp[i] = dp[j]+1
print(N-max(dp))
