from collections import deque


def BFS(start):
    queue = deque()
    visited = []
    start_to_dest = [0 for _ in range(N+1)]

    queue.append(start)

    while queue:
        node = queue.popleft()
        visited.append(node)

        for i in friend_relations[node]:
            if i != start and start_to_dest[i] == 0:
                start_to_dest[i] = start_to_dest[node] + 1
                queue.append(i)
    return sum(start_to_dest)


N, M = map(int, input().split())

friend_relations = [[]for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    friend_relations[u].append(v)
    friend_relations[v].append(u)
result = [N*M+1]
for i in range(1, N+1):
    result.append(BFS(i))
print(result.index(min(result)))
print(result)