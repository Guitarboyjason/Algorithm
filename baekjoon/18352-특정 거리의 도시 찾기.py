import heapq

N, M, K, X = map(int, input().split())

graph = {i+1: [] for i in range(N)}

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

weight = [M+1 for _ in range(N+1)]
weight[X] = 0
q = [[0, X]]
while q:
    w, n = heapq.heappop(q)
    for i in graph[n]:
        if weight[i] > w+1:
            weight[i] = w+1
            heapq.heappush(q, [weight[i], i])
# print(q)
# print(weight)
if K in weight:
    for index, i in enumerate(weight):
        if i == K:
            print(index)
else:
    print(-1)
