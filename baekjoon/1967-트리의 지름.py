#다익스트라로 노드간의 간선 길이를 비교해 보자
#부모 자식 상관없이 양방향 연결 이라고 생각한다면
#하지만 모든 노드에 대해서 지름을 판단해야 하므로 문제가 있다.
#무조건적으로 부모노드를 거치는 것이 좋은것도 아니다.

# n = int(input())
# graph = list([]for _ in range(n+1))
# for _ in range(n):
#     parent,child,cost = map(int,input().split())
#     graph[parent].append([child,cost])
#     graph[child].append([parent,cost])
    
from collections import deque
n = int(input())

relations = {i : dict() for i in range(1,n+1)}

for i in range(n-1):
    u,v,w = map(int,input().split())
    relations[u][v] = w
    relations[v][u] = w
    
children = {i : [] for i in range(1,n+1)}

parents = deque([1])
visited = []
while parents:
    node = parents.popleft()
    if node not in visited:
        visited.append(node)
        for i in relations[node]:
            if i not in visited:
                children[node].append(i)
                parents.append(i)

print(children)