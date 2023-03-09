# 현재 시각
# 요리하는데 필요한 시간
# 종료되는 시각의 시와 분

time = list(map(int,input().split()))
cooking_time = int(input())
cooking_time = [cooking_time//60, cooking_time%60]

if time[1] + cooking_time[1] >= 60:
    time[1] = time[1]+cooking_time[1] - 60

    if time[0] + cooking_time[0] + 1 >= 24:
        time[0] = time[0] + cooking_time[0] + 1 - 24
    else:
        time[0] += (cooking_time[0] + 1)
else:
    time[1] += cooking_time[1]
    if time[0] + cooking_time[0] >= 24:
        time[0] = time[0] + cooking_time[0] - 24
    else:
        time[0] += (cooking_time[0])

for i in time:
    print(i,end=' ')
