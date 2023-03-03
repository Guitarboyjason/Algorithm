N,M = map(int,input().split())
A = [list(map(int,input().split()))for _ in range(N)]
M,K = map(int,input().split())
B = [list(map(int,input().split()))for _ in range(M)]

answer = []

tmp = []
for i in range(N):
    for j in range(M):
        tmp = []
        for k in range(K):
            tmp.append(A[i][j]*B[j][k])
        answer.append(tmp)
    
print(answer)