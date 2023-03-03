# # 00과 1의 조합으로 얼마나 많은 경우의 수가 나올 수 있는가
# from itertools import permutations


# N = int(input())
# count_00 = N//2
# count_1 = N%2

# count_possible = 0

# for i in range(count_00+1):
#     tmp = list(0 for _ in range(count_00-i)) +list(1 for _ in range(count_1+2*i))
#     print(set(permutations(tmp,len(tmp))))
#     count_possible += len(set(permutations(tmp,len(tmp))))
    
#     count_possible %= 15746
# print(count_possible)


# 1 - 1
# 2 - 2
# 3 - 3
# 4 - 5

# 점화식 문제

import sys
sys.setrecursionlimit = 10**7

N = int(input())
dp = [0] * 1000001
dp[1] = 1
dp[2] = 2
for k in range(3,N+1):
    dp[k] = (dp[k-1]+dp[k-2])%15746
print(dp[N])