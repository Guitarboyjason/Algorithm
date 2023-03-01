
import heapq
V, E = map(int, input().split())
K = int(input())
cost = [3000000 for _ in range(V+1)]
cost[K] = 0
graph = {i+1: {} for i in range(V)}
for _ in range(E):
    u, v, w = map(int, input().split())
    if not v in graph[u] or graph[u][v] > w:
        graph[u][v] = w
hq = [[0, K]]
while hq:
    weight, node = heapq.heappop(hq)
    for i in graph[node]:
        # print(i)
        if cost[i] > weight + graph[node][i]:
            cost[i] = weight + graph[node][i]
            heapq.heappush(hq, [cost[i], i])
        # if cost[v] > cost[node]+w:
        #     cost[v] = cost[node]+w
        #     for i in graph[node]:
        #         heapq.heappush(hq, i[0])

for i in range(1, V+1):
    if cost[i] == 3000000:
        print("INF")
    else:
        print(cost[i])


# heapq.heapify(graph)
# print(graph)
