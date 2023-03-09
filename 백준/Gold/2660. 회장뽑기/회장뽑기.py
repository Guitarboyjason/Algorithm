from collections import deque

def bfs(graph,root,members):
    queue = deque([root])
    friend_count = [-1]+[members for _ in range(members)]
    friend_count[root] = 0
    # visited = []
    while queue:
        node = queue.popleft()
       
            # visited.append(node)
        for i in graph[node]:
            if friend_count[i] > friend_count[node] + 1:
                friend_count[i] = friend_count[node] + 1
                queue.append(i)
    return max(friend_count)

members = int(input())

graph = {}
for i in range(1,members+1):
    graph[i] = []
a,b = map(int,input().split())
while a!= -1 and b != -1:
    graph[a].append(b)
    graph[b].append(a)
    a,b = map(int,input().split())
    

chairman_list = []
chairman_count = members
for i in graph.keys():
    tmp = bfs(graph,i,members)
    if tmp < chairman_count:
        chairman_count= tmp
        chairman_list = [i]
    elif tmp == chairman_count:
        chairman_list.append(i)
chairman_list.sort()
print("{} {}".format(chairman_count,len(chairman_list)))
print(*chairman_list)
