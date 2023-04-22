import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N_relations = int(input())

dp = [[0,1] for _ in range(N_relations+1)]
graph = [[]for _ in range(N_relations+1)]
for _ in range(N_relations-1):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False for _ in range(N_relations+1)]
root = 1
def dfs(root):
    global visited
    global graph
    global dp
    visited[root] = True
    for next in graph[root]:
        if visited[next] == False:
            dfs(next)
            dp[root][0] += dp[next][1]
            dp[root][1] += min(dp[next])
dfs(root)
print(min(dp[root]))