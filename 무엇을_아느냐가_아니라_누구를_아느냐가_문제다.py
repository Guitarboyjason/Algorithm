# """
# 최측근 [1]
# 측근 [2]
# 비즈니스관계 [3]
# 지인 [4]

# 이 네가지중 반드시 하나
# 최고의원을 만나기까지의 인맥간 친밀도의 합을 최소화 -> 최소경로


# """

# for T in range(1, int(input()) + 1):
#     N, M = map(int, input().split())
#     graph = [[100 for _ in range(M)] for _ in range(M)]  # 친밀한 정도
#     for _ in range(N):
#         x, y, z = map(int, input().split())
#         graph[x][y] = z
#         graph[y][x] = z

#         # for i in range(M):
#         #     for j in range(M):
#         #         for k in range(M):
#         #             if i != j and i != k and j != k:
#         #                 if graph[i][j] == -1 or graph[i][j] > graph[i][k] + graph[k][j]:
#         #                     graph[i][j] = graph[i][k] + graph[k][j]

#     answer = []
#     # if graph[0][M-1] != 100:
#     answer = [0, M - 1]
#     flag = 1 if graph[0][M - 1] != 100 else 0
#     while True:
#         tmp = answer.copy()
#         i = 0
#         while True:
#             change_list = []
#             for j in range(M):
#                 if (
#                     graph[answer[i]][answer[i + 1]]
#                     > graph[answer[i]][j] + graph[j][answer[i + 1]]
#                 ):
#                     change_list.append(
#                         [j, graph[answer[i]][j] + graph[j][answer[i + 1]]]
#                     )
#             if change_list:
#                 answer.insert(i + 1, min(change_list, key=lambda x: x[1])[0])
#             i += 1
#             if i >= len(answer) - 2:
#                 break
#         if tmp == answer:
#             break

#     print(f"Case #{T}: ", end="")
#     if answer == [0, M - 1] and not flag:
#         print(-1)
#     else:
#         print(*answer)

import heapq

INF = float("inf")


def dijkstra(graph, start):
    distance = {node: INF for node in graph}
    distance[start] = 0
    queue = []
    heapq.heappush(queue,[distance[start],start])
    
    while queue:
        dist,dest = heapq.heappop(queue)
        if distance[dest] < dist:
            continue
        for n_dist,n_dest in distance[dest].items():
            