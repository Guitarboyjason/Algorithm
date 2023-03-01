# # # 기본적으로 가장 긴 길이를 구하려면 각 노드에서 각 노드로의 거리를 알아야 한다.
# # # 그러려면 시간복잡도 때문에 제대로 돌아갈지 모르겠는데
# # # 자식이 있는 노드들은 최대 지름이 될 수 없다.
# # # 자식이 없는 노드들만 확인 해 보자

# # import heapq

# # n = int(input())
# # graph = {i: [] for i in range(1, n+1)}

# # for _ in range(n-1):
# #     u, v, w = map(int, input().split())
# #     graph[u].append([w, v])
# #     graph[v].append([w, u])

# # max_len = 0
# # childrens = [i for i in graph if len(graph[i]) == 1]
# # for i in childrens:
# #     if len(graph[i]) > 1:
# #         continue
# #     hq = [i]
# #     dict_len = {j: 1000001 for j in range(1, n+1)}
# #     dict_len[i] = 0
# #     # print(dict_len)
# #     while hq:
# #         node = heapq.heappop(hq)
# #         for w, j in graph[node]:
# #             if dict_len[j] > dict_len[node] + w:
# #                 dict_len[j] = dict_len[node] + w
# #                 heapq.heappush(hq, j)
# #     i_max_len = max(dict_len.values())
# #     if max_len < i_max_len:
# #         max_len = i_max_len

# # print(max_len)
# # 다이나믹 프로그래밍으로 해결 할 수 있을 것 같은데...?
# # 관계가 하나뿐인 노드들을 queue에 담는다
# # 각 부모에 해당 노드로 가는 간선의 w를 전달..
# # 근데 그 다음 노드에서 부모를 어떻게 찾을까

# # 1이 기본적으로 최상위 노드니까 여기서부터 출발할까
# # 그럼 재귀로 해서 최상위 노드부터 자식 노드를 확인 - 확인 된 노드들은 더 이상 확인하지 않게 visited에 넣는걸로

# from collections import deque


# def dfs(graph, root):
#     children = deque([i[1] for i in graph[root]])
#     visited = [root]
#     while children:
#         node = children.popleft()
#         if node not in visited:
#             visited.append(node)
#             node_children = graph[node]
#             for w, v in node_children:
#                 # len_graph[node] += len_graph[node] +
#                 if v not in visited:
#                     len_graph[v] += len_graph[node] + w
#                     children.append(v)


# n = int(input())
# graph = {i: [] for i in range(1, n+1)}
# len_graph = {i: 0 for i in range(1, n+1)}
# for _ in range(n-1):
#     u, v, w = map(int, input().split())
#     graph[u].append([w, v])
#     graph[v].append([w, u])
# dfs(graph, 1)
# # print(len_graph)
# max_len = max(len_graph.items(), key=lambda x: x[1])
# # second_max_len = max(len_graph.values(), key=lambda x: x != max_len)
# second_max_len = max([i for i in len_graph.items() if i != max_len])
# # print(max_len + second_max_len)
# # print(max_len)
# # print(second_max_len)
# print(max_len[1] + second_max_len[1])


# 부모를 따로 저장해두자
# 제일 말단부터 올라오는 식으로
from collections import deque
n = int(input())
graph = {i: {} for i in range(1, n+1)}
parents = {i: -1 for i in range(1, n+1)}
weights = {i: {j: 0 for j in range(1, n+1) if j != i} for i in range(1, n+1)}

for _ in range(n-1):
    u, v, w = map(int, input().split())
    graph[u][v] = w
    graph[v][u] = w

# 부모 먼저 찾자
parent_queue = deque([1])
parent_visited = []
while parent_queue:
    node = parent_queue.popleft()
    if node in parent_visited:
        continue
    parent_visited.append(node)
    for i in graph[node]:
        # for j in i:
        # if i[0] == node:
        if i not in parent_visited:
            parents[i] = node
            parent_queue.append(i)
        # parent_visited.append(i)
# print(parents)

# len_from_children = {i : }

visited = []
queue = deque([i for i in graph.keys() if len(graph[i]) == 1])

while queue:
    node = queue.popleft()
    # if node in visited:
    #     continue
    # visited.append(node)
    if node == 1:
        continue
    # parent = parents[node]
    # for v, w in graph[node]:
    #     # if v not in visited:
    #     if max(weights[v]) < max(weights[node])+w:
    #         weights[v].append(max(weights[node]) + w)
    #         # weights[v] < weights[node] + w:
    #         # weights[v] = weights[node] + w
    #         queue.append(v)
    parent = parents[node]
    w = graph[node][parent]
    # for i in graph[node]:
    #     if i == parent:
    #         w = graph[node][i]
    # if max(weights[parent]) < max(weights[node])+w:
    #     weights[parent].append(max(weights[node]) + w)
    #     queue.append(parent)
    weights[parent][node] = max(weights[node].values())+w
    queue.append(parent)


# queue = deque([1])
# while queue:
#     node = queue.popleft()
#     children = [i[0] for i in parents.items() if i[1] == node]
#     # print(children)
#     for child in children:
#         weights[child] += weights[node] + graph[node][child]
#         queue.append(child)


# print(weights)
# print(weights.items())
# for i in weights.items():
#     print(sum(i[1].values()))
# print(max(sum(i) for i in weights.values()))

print(max([sum(i[1].values()) for i in weights.items()]))
# print(max(weights.items(), lambda x: sum(x[1].values())))
# print(weights.items())
