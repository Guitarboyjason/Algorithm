import sys

def printing(dp,n,cost):
    for i in range(n):
        if i ==0 :
            dp[i][0] = cost[i][0]
            dp[i][1] = cost[i][1]
            dp[i][2] = cost[i][2]
            continue;
        
        dp[i][0] = cost[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = cost[i][1] + min(dp[i-1][0],dp[i-1][2])
        dp[i][2] = cost[i][2] + min(dp[i-1][0],dp[i-1][1])

    min_cost = min(dp[n-1][0],dp[n-1][1])
    min_cost = min(min_cost ,dp[n-1][2])
    return min_cost

n = int(input())
cost = []
for i in range(n):
    tmp = list(map(int,input().split()))
    cost.append(tmp)
    dp = [[-1]*3 for _ in range(n+1)]
print(printing(dp,n,cost))
        
