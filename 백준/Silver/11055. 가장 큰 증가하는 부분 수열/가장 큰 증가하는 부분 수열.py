# 증가 부분 수열 중 합이 가장 큰 것.

N = int(input())
A = list(map(int ,input().split()))
dp = [i for i in A]
for i in range(1,N):
    for j in range(i):
        if A[j] < A[i]:
            if dp[i] < dp[j] + A[i]:
                dp[i] = dp[j] + A[i]
print(max(dp))