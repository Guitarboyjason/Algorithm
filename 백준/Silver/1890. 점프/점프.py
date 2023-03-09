# # 임의의 한 칸에서 한번만에 도착을 할 수 있다 가정을 하자.
# # 그럼 해당 타일에서 0까지 도착할 수 있는 경우의 수는 1
# # 그렇다면 해당 타일까지 도달할 수 있는 경우의 수 만큼 경로가 생기게 된다.
# # 0으로 도달하는 경우 멈춰버리기 때문에 무조건 피해야 한다.
# # 아니면 그냥 아예 도달 할 수 없는 타일들을 -1으로 바꿔버리자.
# # 그리고 도달 할 수 있는 타일들은 -2로 바꾸자
#
# # def find_way(arr,x,y):
# #     if arr[y,x] + x <= N-1 and arr[y,x] + y <= N+1:
# #         if arr[y,x+arr[y,x]] == -1 and arr[y+arr[y,x],x] == -1:
# #             arr[y,x] = -1
# #         elif arr[y,x+arr[y,x]] == -2 or arr[y+arr[y,x],x] == -2:
# #             arr[y,x] = -2
# #     elif arr[y,x] + x <= N-1:
# #         if arr[y,x+arr[y,x]] == -1:
# #             arr[y,x] = -1
# #         elif
#
#
#
# # def find_way_2(y,x):
# #     if x == y == N-1:   #끝에 도달 했을 때
# #         return 1
# #     elif x >= N or y >= N:  #넘어가버렸을 때
# #         return 0
# #     else:
# #         return (find_way_2(y+arr[y][x],x)+find_way_2(y,x+arr[y][x]))
#
# def find_way_3(y,x):
#     if way_arr[y][x] != -1:
#         way_arr[y][x] += 1
#         return way_arr[y][x]
#     else:
#         if y == x == N-1:
#             return 1
# N = int(input())
# arr = []
# way_arr = [[-1]*(N+1)] * (N+1)
#
# for _ in range(N):
#     arr.append(list(map(int,input().split())))
# print(find_way_2(0,0))


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
# for i in cnt_way:
#     print(i,end='\n')
print(cnt_way[N][N])
