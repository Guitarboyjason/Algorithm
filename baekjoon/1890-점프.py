# 초기값을 0으로 초기화한 길이가 N인 배열을 선언.
# 출발지만 1로 값을 주고 모든 배열에 대해 그 배열에 쓰여있는 값만큼을
# 오른쪽이나 아래로 움직여서 움직이기 전 적혀있던 값을 더해준다.


N = int(input())
arr = [[-1 for i in range(N+1)] for j in range(N+1)]
for i in range(N):
    tmp = list(map(int,input().split()))
    for j in range(N):
        arr[i+1][j+1] = tmp[j]

cnt_way = [[0 for i in range(N+1)] for j in range(N+1)]
cnt_way[1][1] = 1

for i in range(1,N+1):
    for j in range(1,N+1):
        if i == j == N:
            break
        tmp = arr[i][j]
        if i + tmp <= N:        #아래로 확인
            cnt_way[i+tmp][j] += cnt_way[i][j]
        if j + tmp <= N:
            cnt_way[i][j+tmp] += cnt_way[i][j]
print(cnt_way[N][N])
