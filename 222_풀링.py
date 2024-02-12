import sys

input = sys.stdin.readline


def pooling(graph, N):
    if N == 1:
        return graph[0][0]

    n_graph = [[] for _ in range(N // 2)]
    for i in range(0, N, 2):
        for j in range(0, N, 2):
            arr = [graph[i][j], graph[i][j + 1], graph[i + 1][j], graph[i + 1][j + 1]]
            arr.sort()
            n_graph[i // 2].append(arr[-2])
    return pooling(n_graph, N // 2)


N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]
print(pooling(graph, N))
