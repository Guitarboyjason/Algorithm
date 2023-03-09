from collections import deque


def dfs(start, end):
    stack = deque()
    stack.append(start)
    while stack:
        node = stack.pop()
        if node == end:
            return cnt[node]
        for i in graph[node]:
            if cnt[i] == 0:
                cnt[i] = cnt[node]+1
                stack.append(i)
    return -1


n = int(input())
cnt = [0 for _ in range(n+1)]
people1, people2 = map(int, input().split())

people_relations = [list(map(int, input().split()))
                    for _ in range(int(input()))]
# print(people_relations)
graph = [[]for _ in range(n+1)]
# print(graph)
for i in people_relations:
    graph[i[0]].append(i[1])
    graph[i[1]].append(i[0])
# print(graph)
print(dfs(people1, people2))
