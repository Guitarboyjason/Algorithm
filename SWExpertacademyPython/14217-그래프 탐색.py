import sys
sys.stdin = open("SWExpertacademyPython/input.txt")
input = sys.stdin.readline
def dfs(root):
    if root == 1:
        return 0
    else:
        cnt = 0
        stack = [(root,0)]
        # visited = [(root,0)]
        visited = {i : -1 for i in range(1,n+1)}
        visited[i] = 0
        while stack:
            node,c_cnt = stack.pop()
            if node == 1:
                return c_cnt
            for neighbor in graph[node]:
                if (neighbor,c_cnt+1) not in visited:
                    visited.append((neighbor,c_cnt+1))
                    stack.append((neighbor,c_cnt+1))
        return -1
n,m = map(int,input().split())
graph = {i:[] for i in range(1,n+1)}
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
q = int(input())
for _ in range(q):
    a,i,j = map(int,input().split())
    if a == 1:
        graph[i].append(j)
        graph[j].append(i)
    else:
        graph[i].remove(j)
        graph[j].remove(i)
    # dfs()
    print(*[dfs(i) for i in range(1,n+1)])