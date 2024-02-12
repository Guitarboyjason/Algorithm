N = int(input())

consult = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)] + [[0, 0]]
dp = [0 for _ in range(N + 2)]
for i in range(1, N + 2):  # 1일부터 N일까지
    t, p = consult[i]
    dp[i] = max(dp[i - 1], dp[i])
    if i + t <= N + 1:
        dp[i + t] = max(dp[i + t], dp[i] + p)
print(dp[-1])
