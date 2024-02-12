# from collections import dict
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
# worked = [False for _ in range(M)]
worked = set()
graph = dict()
for _ in range(N): # 할때마다 sort? len을 기준으로? 계속 update하는거 어때 시간적으로 손해 많이 볼 것 같은데 가능한 갯수들 별로 dic으로 묶고,
                   # 얘네를 가능한 set들을 나타내, 그 set별로 또 dic으로 묶는다? 아니면 그 가능한 수들로 묶인 애들을 다시 갯수로 내림차순..? 계속 업데이트 하면서?
    count , *arg = map(int,input().split())
    if count not in graph:
        graph[count] = [set(arg)]
    else:
        graph[count].append(set(arg))
    # # print(count, arg)
    # {count : arg for (count,*arg) in map(int,input().split())}

print(graph)

cnt = 0
for i in range(1,M):
    # print(i)
    if i in graph:
        working_directory = graph[i]
        working_directory = sorted([i-worked for i in working_directory],key=lambda x : len(x))
        for j in range(len(working_directory)):
            