
dp = [0] + [1 for _ in range(9)]
dp2 = [0 for _ in range(10)]


N = int(input())
for _ in range(N-1):
    for i in range(10):
        if i == 0:
            dp2[i] = dp[1]
        elif i == 9:
            dp2[i] = dp[8]
        else:
            dp2[i] = dp[i-1]+dp[i+1]
    dp = [i for i in dp2]
print(sum(dp))