"""
한 학기에 들을 수 있는 과목 수에는 제한이 없다.
모든 과목은 매 학기 항상 개설된다.
"""
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = {i: [] for i in range(1, N + 1)}
topology_nums = [0 for i in range(N + 1)]
for _ in range(M):
    before, after = map(int, input().split())
    graph[before].append(after)
    topology_nums[after] += 1

queue = deque()
for i in range(1, N + 1):
    if topology_nums[i] == 0:
        queue.append(i)
# queue.extend([graph[i] for i in graph if topology_nums[i] == 0])
from copy import deepcopy

visited = []
answer = {i: -1 for i in range(1, N + 1)}
semester = 1
for semester in range(1, N + 1):
    for node in queue:
        answer[node] = semester
    semester += 1
    # while queue:  #  0이 되면 추가
    t_queue = deque()
    while queue:
        node = queue.popleft()
        for next in graph[node]:
            topology_nums[next] -= 1
            if topology_nums[next] == 0:
                t_queue.append(next)
    queue = deepcopy(t_queue)
# print(answer)
# for i in answer:
# print(answer[i])

# for i in answer.values():
#     print(i)
print(*[i for i in answer.values()])
