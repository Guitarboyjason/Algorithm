# 다이나믹 프로그래밍으로 해당 위치까지 도착했을 때의 가장 큰 합을 저장한다.

n = int(input())
perms = list(map(int,input().split()))
max_add = [0 for _ in range(n)]
max_add[0] = perms[0]
for i in range(1,n):
    if perms[i] > max_add[i-1] + perms[i]:
        max_add[i] = perms[i]
    else:
        max_add[i] = max_add[i-1] + perms[i]
print(max(max_add))