N, M, A, B = map(int, input().split())

dp = [100_001 for _ in range(N + 1)]

for _ in range(M):
    L, R = map(int, input().split())
    for i in range(L, R + 1):
        dp[i] = -1

dp[0] = 0
for i in range(N + 1):
    if dp[i] != -1:
        if i + A <= N and dp[i + A] != -1 and dp[i + A] > dp[i] + 1:
            dp[i + A] = dp[i] + 1
        if i + B <= N and dp[i + B] != -1 and dp[i + B] > dp[i] + 1:
            dp[i + B] = dp[i] + 1

# print(dp)
if dp[-1] == 100_001:
    print(-1)
else:
    print(dp[-1])

print(dp)
