# 전체 가수의 순서를 정하는 것
# 모든 조건을 만족하는 것이 불가능할 수도 있다.
# 불가능 할 경우 0을 출력
# 그래프...?

import sys
from collections import deque

input = sys.stdin.readline
num_singer, num_pd = map(int, input().split())

graph_out = {i: [] for i in range(1, num_singer + 1)}
topology_nums = [0 for _ in range(num_singer + 1)]
for _ in range(num_pd):
    n_singer, *args = map(int, input().split())
    # print(args)
    for i in range(len(args) - 1):
        graph_out[args[i]].append(args[i + 1])  # 나중에 나와야 할 것
        topology_nums[args[i + 1]] += 1
queue = deque()
answer = []
visited = []
while len(answer) < num_singer:
    if 0 not in topology_nums[1:]:
        print(0)
        break
    # print(topology_nums)
    queue.extend(
        [
            idx
            for idx, i in enumerate(topology_nums)
            if idx != 0 and i == 0
            if idx not in visited
        ]
    )
    while queue:
        node = queue.popleft()
        # if node not in visited:
        answer.append(node)
        visited.append(node)
        for next in graph_out[node]:
            topology_nums[next] -= 1
            if topology_nums[next] == 0:
                
else:
    for i in answer:
        print(i)


# else:
#     pass
# while len(answer) < num_singer:
#     for i in graph_in:  # 나중에 업데이트도 해줘야겠네
#         if i not in visited:
#             if len([j for j in graph_in[i] if j not in visited]) == 0:
#                 queue.append(i)
#                 visited.append(i)

#     while queue:
#         node = queue.popleft()
#         answer.append(node)
# # print(visited)
# # print(answer)
# for i in answer:
#     print(i)
