# 자신의 모든 친구들이 얼리 아답터일때만 얼리 아답터가 된다.
# 트리 구조인 경우, -> 모든 두 정점 사이에 이들을 잇는 경로가 존재하면서 사이클이 존재하지 않는 경우만 고려

# 친구 관계 트리가 주어졌을 대, 모든 개인이 새로운 아이디어를 수용하기 위해 필요한 최소 얼리 어답터의 수를 구하는 프로그램
# 일자로 늘어져있는 경우, 한명만 얼리어답터면 모든 사람이 얼리 어답터가 된다.
# 그러므로 일자로 이루어진 사람들은 한명만 있다고 봐도 무방하다. --> 아님.

# 하지만 분기점이 생긴다면..? 해당 두 갈래만큼의 사람이 필요하다..,? 이건 또 아닌것 같은데

# parent_to_child_tree = {i :[] for i in range(1,N_relations+1)}
# child_to_parent_tree = {i :[] for i in range(1,N_relations+1)}
# for _ in range(N_relations):
#     u,v = map(int,input().split())
#     parent_to_child_tree[u].append(v)
#     child_to_parent_tree[v].append(u)
    
# root = -1
# for node in child_to_parent_tree.items():
#     if len(node[1]) == 0:
#         root = node[0]

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