A,B =input().split()
# A가 B의 어느 위치에서 가장 비슷한가.

N = len(A)
M = len(B)
min_diff = 50
for i in range(M-N+1):
    tmp_diff = 0
    for j in range(N):
        if A[j] != B[i+j]:
            tmp_diff += 1
    if tmp_diff < min_diff:
        min_diff = tmp_diff
print(min_diff)