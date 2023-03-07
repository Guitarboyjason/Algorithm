import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def cal_building_time(building):
    if dp[building] != -1:
        return dp[building]
    if not building_rules[building]:
        dp[building] = building_time[building]
        return dp[building]
    else:
        befores = [cal_building_time(i) for i in building_rules[building]]
        dp[building] = max(befores) + building_time[building]
        return dp[building]
        
for T in range(int(input())):
    N,K = map(int,input().split())
    building_time = [-1]+list(map(int,input().split()))
    # building_rules = [list(int,input().spi)]
    building_rules = {i:[] for i in range(1,N+1)}
    for _ in range(K):
        first,second = map(int,input().split())
        building_rules[second].append(first)
    W = int(input())
    dp = [-1] * (N+1)
    print(cal_building_time(W))