N, M = map(int, input().split())

A = []
for i in range(N):
    A.append(list(map(int, input().split())))
for i in range(N):
    tmp_list = list(map(int, input().split()))
    for j in range(M):
        A[i][j] += tmp_list[j]
for i in range(N):
    for j in range(M):
        print(A[i][j], end=" ")
    print()
