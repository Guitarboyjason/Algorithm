# import heapq
# n = int(input())
# wine = [int(input()) for _ in range(n)]
# # 바로 앞의 와인을 마셨을 경우, 그렇지 않은 경우
# dp = [[0, i] for i in wine]
# dp[1][0] = -(wine[0] + wine[1])
# queue = []
# for i in range(2, n):
#     # dp[i][1] = wine[i-1] + wine[i]
#     # dp[i][0] = max(dp[i-2]) + wine[i]
#     dp[i][0] = dp[i-1][1] + wine[i]
#     dp[i][1] = max(max(dp[:i-1], key=lambda x: max(x))) + wine[i]
# # print(wine)
# # print(dp)
# print(max(max(dp, key=lambda x: max(x))))

import heapq

n = int(input())
wine = [int(input())for _ in range(n)]

hqueue = []
# heapq에 값을 집어 넣을 건데 두번째 전 애들을 계속 집어넣자
#
# 바로 앞의 와인을 마신 경우, 아닌 경우
dp = [[0, 0] for _ in range(n)]
dp[0] = [wine[0], wine[0]]
if n >= 2:
    dp[1] = [wine[0]+wine[1], wine[1]]

for i in range(2, n):
    heapq.heappush(hqueue, -max(dp[i-2]))
    dp[i][0] = dp[i-1][1] + wine[i]
    dp[i][1] = -hqueue[0] + wine[i]
print(max(max(dp, key=lambda x: max(x))))
