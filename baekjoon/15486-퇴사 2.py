# import heapq
import sys
input = sys.stdin.readline
N = int(input())
consulting = [list(map(int,input().split()))for _ in range(N)]
# print(consulting)

consulting.reverse()
# print(consulting)
dp = [0] + [i[1] for i in consulting]
# print(dp)
# queue = [0]
for remain in range(1,N+1):
    time,pay = consulting[remain-1]
    if time > remain:
        dp[remain] = dp[remain-1]
    else:
        # if time != remain:
        #     # 여기를 시간 복잡도를 줄일 수 있을 것 같음.
        #     dp[remain] = max(dp[:remain-time+1])
        
        # else:       # 선택하거나 아니거나 이걸 먼저 해줄까
        #     dp[remain] = max(dp[:remain],consulting[remain][1])
        # if remain-time >= 0:
        dp[remain] += dp[remain-time]#, dp[:remain])
        # print(queue[0])
        dp[remain] = max(dp[remain],dp[remain-1])
    # heapq.heappush(queue,-dp[remain])
print(dp[-1])
