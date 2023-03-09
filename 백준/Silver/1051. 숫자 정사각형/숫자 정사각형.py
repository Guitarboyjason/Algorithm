N, M = map(int, input().split())

graph = [input() for _ in range(N)]

max_len = min(N, M)
max_size = 1
for i in range(N):
    for j in range(M):
        column_max = M-j
        row_max = N-i
        for k in range(1, min(column_max, row_max)):
            if graph[i][j] == graph[i+k][j] == graph[i][j+k] == graph[i+k][j+k]:
                if max_size < (k+1)**2:
                    max_size = (k+1)**2
print(max_size)
