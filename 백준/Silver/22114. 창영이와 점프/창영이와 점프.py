# 최대한 빨간 보도블럭만
# 한번에 k만큼 이동 가능
# 최대 한번 거리에 상관 없이 i 에서 i+1로 이동할 수 있다...?
# 만약 다음 블럭을 밟을 수 없다면 거기서 끝
# 최적의 시작점을 찾아 최고기록을 세우고 싶다.최대 몇개의 블럭을 연속적으로 밟을 수 있을까

N,K = map(int,input().split())
blocks = list(map(int,input().split()))

## K보다 작은 노드들이 최대 몇개가 나오는가... 

dp = [[0,0] for _ in range(N)]  #총 몇개가 필요하지 N개가 필요하겠다.
# [건너뛰지 않음, 건너뜀]
dp[0] =  [1,0]

for i in range(1,N):
    if blocks[i-1] > K:   #기회를 써야한다.
        dp[i] = [1,dp[i-1][0]+1]
    else:
        dp[i] = [dp[i-1][0]+1,dp[i-1][1]+1]
        
print(max(max(i)for i in dp))
        


