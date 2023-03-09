
from copy import deepcopy
n = int(input())
m = int(input())
graph = {}
for i in range(n):
    graph[i+1] = []
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

sang_friends = graph[1]
invited = deepcopy(graph[1])
for i in sang_friends:
    invited.extend(graph[i])
    # print(invited)
invited = set(invited)
if 1 in invited:
    invited.remove(1)
print(len(invited))