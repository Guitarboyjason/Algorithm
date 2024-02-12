import sys
input = sys.stdin.readline

def find_most_hacking_node():
    most_list=[]
    most_cnt = 0
    for i in graph:
        tmp = dfs(i)
        if tmp > most_cnt:
            most_list = [i]
            most_cnt = tmp
        elif tmp == most_cnt:
            most_list.append(i)
    return most_list

def dfs(root):
    stack = [root]
    visited = {i : False for i in range(1,N+1)}
    visited[root] = True
    cnt = 1
    while stack:
        node =  stack.pop()
        for child in graph[node]:
            if visited[child] == False:
                visited[child] = True
                cnt += 1
                stack.append(child)
                
    return cnt

N,M = map(int,input().split())
graph = {i : [] for i in range(1,N+1)}

for _ in range(M):
    A,B = map(int,input().split())
    graph[B].append(A)
print(*find_most_hacking_node())