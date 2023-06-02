import sys
inpurt = sys.stdin.readline
for _ in range(int(input())):
    N = int(input())
    price = list(map(int,input().split()))
    answer = 0
    
    dp = [-1 for _ in range(N)]
    maximum = -1
    for i in range(N-1,-1,-1):
        if maximum < price[i]:
            maximum = price[i]
        dp[i] = maximum
    
    for i in range(N-1):
        if price[i] < dp[i]:
            answer += dp[i] - price[i]
    print(answer)