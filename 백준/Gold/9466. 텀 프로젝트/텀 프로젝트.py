import sys
sys.setrecursionlimit(111111)

def dfs(x):
    global result
    visited[x] = True
    cycle.append(x)
    next = choose[x]

    if visited[next]:
        if next in cycle:
            result += cycle[cycle.index(next):]
        return
    else:
        dfs(next)


for _ in range(int(input())):
    N = int(input())
    choose = [0] + list(map(int,input().split()))
    visited = [True] + [False]*N
    result = []

    for i in range(1,N+1):
        if not visited[i]:
            cycle = []
            dfs(i)
    print(N - len(result))
