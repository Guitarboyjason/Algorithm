from collections import deque

N, K = map(int, input().split())

dp = [-1 for _ in range(K * 2 + 1)]
dp[N] = [N]
for i in range(N - 1, -1, -1):
    dp[i] = dp[i + 1] + [i]
for i in range(1, K):
    if dp[i + 1] == -1 or len(dp[i + 1]) > len(dp[i]) + 1:
        dp[i + 1] = dp[i] + [i + 1]
    if dp[i - 1] == -1 or len(dp[i - 1]) > len(dp[i]) + 1:
        dp[i - 1] = dp[i] + [i - 1]
    if dp[i * 2] == -1 or len(dp[i * 2]) > len(dp[i]) + 1:
        dp[i * 2] = dp[i] + [i * 2]

print(len(dp[K]))
print(*dp[K])


# queue = deque()
# # queue.appendleft(K)
# # while N != K:
# #     if K + 1 == N:
# #         K += 1
# #     elif K - 1 == N:
# #         K -= 1
# #     else:
# #         if K > N:
# #             if K % 2 == 1:
# #                 K -= 1
# #             else:
# #                 K //= 2
# #         else:
# #             K += 1
# #     queue.appendleft(K)
# print(len(queue) - 1)
# print(*queue)
