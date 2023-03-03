# 일을 승락하여 페이를 받는다면, 일을 하고 있는 중간의 일들은 다 못하게된다.


N = int(input())

schedule = [[-1,-1]] # 초기값
max_cost = [-1]*(N+1)

for _ in range(N):
    T,P = map(int,input().split())
    schedule.append([T,P])

for i in range(1,N+1):
    if i + schedule[i][0] <= N:
        max_cost[i + schedule[i][0]] = \
            max(max_cost[i + schedule[i][0]]+ schedule[i + schedule[i][0]][1],
                max_cost[i + schedule[i][0]])
print(max_cost[7])
