# 5 (4,3) (3,2) (2,1) (2,1)
# 6 (5,4)

n = int(input())
dp = [0, 1, 1]
for i in range(3, n+1):
    dp.append(dp[i-1]+dp[i-2])
print(dp[n], n-2)
