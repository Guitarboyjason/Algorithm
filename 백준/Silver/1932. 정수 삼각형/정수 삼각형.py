n = int(input())
graph = [list(map(int, input().split()))for _ in range(n)]
# print(graph)
dp = [[0 for _ in range(n)] for _ in range(n)]
graph.reverse()
# print(graph)
dp[0] = graph[0]
for i in range(1, n):
    for j in range(len(graph[i])):
        dp[i][j] = max(dp[i-1][j], dp[i-1][j+1]) + graph[i][j]
print(dp[n-1][0])
