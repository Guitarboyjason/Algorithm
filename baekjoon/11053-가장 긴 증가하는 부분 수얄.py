N = int(input())
arr = [i for i in int(input().strip().split())]

dp = [-1]*(N+1)
dp[1] = 1

for i in range(2,N+1):
    if arr[i] > arr[i-1]:
        dp[i] = dp[i-1]
    elif arr[i] == min(arr):
        arr[i] = 1
    else:

