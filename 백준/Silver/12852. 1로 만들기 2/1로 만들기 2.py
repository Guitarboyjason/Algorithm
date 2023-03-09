N = int(input())
dp = [[] for _ in range(10**6+1)]
dp[1] = [1]
for i in range(2,N+1):
    dp[i] = [i for i in dp[i-1]]
    if i % 3 == 0:
        dp[i] = [i for i in min(dp[i],dp[i//3],key=lambda x : len(x))]
    if i % 2 == 0:
        dp[i] = [i for i in min(dp[i],dp[i//2],key=lambda x : len(x))]
    dp[i].append(i)
        
print(len(dp[N])-1)
print(*reversed(dp[N]))
