# N, K = map(int, input().split())
# two_list = [2**i for i in range(18)]
# print(two_list)
# cnt = 0
# while K >= 2:
#     if K % 2 == 0:
#         K //= 2
#     else:
#         K -= 1
#         cnt += 1
# while N >= 2:
#     if N % 2 == 0:
#         N //= 2
#     else:
#         N -= 1
#         cnt += 1
# print(cnt)

import heapq
N, K = map(int, input().split())
weight = [300000 for _ in range(2*K+1)]
weight[2*K] = 0
q = [[0, 2*K]]
while q:
    w, node = heapq.heappop(q)
    if node != 2*K:
        if weight[node+1] > w:
            weight[node+1] = w
    if node != 1:
        if weight[node-1] > w:
            weight[node-1] = w
    while node % 2 == 0:

        # if w < weight[node]:
