from collections import deque
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
# works = [list(map)]

graph = {i:[] for i in range(N+1)}
for _ in range(M):
    before,after = map(int,input().split())
    graph[after].append(before)
X = int(input())

cnt = 0
queue = deque()
queue.append(X)
visited = [False for _ in range(N+1)]
visited[X] = True
while queue:
    node = queue.popleft()
    cnt += 1 ## X 도 포함이므로 나중에 -1 을 해주자
    ## 중복을 허용하지 않네
    # queue.extend(graph[node])
    for next in graph[node]:
        if visited[next] == False:
            visited[next] = True
            queue.append(next)
print(cnt-1)