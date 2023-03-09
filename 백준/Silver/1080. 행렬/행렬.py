

N, M = map(int, input().split())

A = [input()for _ in range(N)]
B = [input()for _ in range(N)]

# XOR을 진행해서 얼마나 다른지에 대한 배열을 만든다.

diff = [[False]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if A[i][j] != B[i][j]:
            diff[i][j] = True

# print(A)
# print(B)
# print(diff)
cnt = 0
try:
    for i in range(N):
        for j in range(M):
            if diff[i][j] == True:
                cnt += 1
                for k in range(3):
                    for l in range(3):
                        diff[i+k][j+l] = not diff[i+k][j+l]
    print(cnt)
except:
    print(-1)

# print(diff)
