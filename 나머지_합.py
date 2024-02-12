#1_000_000 시간초과 무조건 나는데...
import sys
input = sys.stdin.readline
from collections import Counter
import math

N ,M= map(int,input().split())
arr =  list(map(int,input().split()))
# print(arr)

dp = [0]+arr
for i in range(1,N+1):
    dp[i] += dp[i-1]
    dp[i] %= M
# print(dp)
cnt = 0
# print(Counter(dp))
for i in Counter(dp).values():
    # print(i)
    cnt += math.comb(i,2)
print(cnt)