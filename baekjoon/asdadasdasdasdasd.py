test = int(input())

def residents(i,j):
    # if i ==0:
    #     return j
    # if j ==1:
    #     return 1
    if dp[i][j] != -1:
        return dp[i][j]
    else:
        dp[i][j] = residents(i-1,j) + residents(i,j-1)
        return dp[i][j]


for i in range(test):
    k = int(input())
    n = int(input())
    dp = [[-1 for i in range(n+1)]for j in range(k+1)]
    dp[0] = [n for _ in range(n+1)]
    print(dp)
    
    print(residents(k,n))
    print(dp)