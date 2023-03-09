N = int(input())
A = list(map(int, input().split()))
dp = [[0, 0] for _ in range(N)]
# [증가,감소]
for i in range(1, N):
    for j in range(i):
        if A[j] < A[i]:
            if dp[i][0] < dp[j][0] + 1:
                dp[i][0] = dp[j][0]+1

for i in range(N-2, -1, -1):
    for j in range(N-1, i, -1):
        if A[j] < A[i]:
            if dp[i][1] < dp[j][1] + 1:
                dp[i][1] = dp[j][1]+1
print(sum(max(dp, key=lambda x: sum(x))) + 1)
