# import sys
# sys.stdin = open("baekjoon/input.txt")
# input = sys.stdin.readline

# sys.setrecursionlimit(10**6)
# def cal_building_time(node):
#     if dp[node] != -1:
#         return dp[node]
#     if node not in need_somebuiling_for_build:
#         dp[node] = building_time[node]
#         return dp[node]
#     need_buildings = [i[0] for i in building_rules if i[1] == node]
#     dp[node] = building_time[node] + max([cal_building_time(building) for building in need_buildings])
#     return dp[node]
    
# for _ in range(int(input())):
#     N,K = map(int,input().split())
#     building_time = [0] + list(map(int,input().split()))
#     building_rules = [list(map(int,input().split()))for _ in range(K)]
#     dp = [-1 for _ in range(N+1)]
#     W = int(input())
#     need_somebuiling_for_build = [i[1] for i in building_rules]
#     print(cal_building_time(W))

# # 어떻게 dp로 풀 수 있을까

# # 내 생각엔 이거임.
# # 똑같은 콬드인데 최단시간을 저장하면 됨
import sys
sys.stdin = open("baekjoon/input.txt","r")
# sys.setrecursionlimit(1000)
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