# # 오른쪽 혹은 아래쪽으로 한 칸씩만 이동 가능
# # 탐사할 영역에 대한 정보가 주어질 때 탐색할 수 있는 자원의 최대 숫자.
#
# # 재귀로 해결 하면 안되겠지..?
#
# N,M = map(int,input().split())
# area = []
# for i in range(N):
#     area.append(list(map(int,input().split())))
#
# def find_mineral(x,y):
#     if area[x][y] == 1:
#         if x != N-1 and y != M-1:
#             return 1 + max(find_mineral(x+1,y),find_mineral(x,y+1))
#         elif x != N-1:
#             return 1 + find_mineral(x+1,y)
#         elif y != M-1:
#             return 1 + find_mineral(x,y+1)
#         else:
#             return 1
#     else:
#         if x != N-1 and y != M-1:
#             return max(find_mineral(x+1,y),find_mineral(x,y+1))
#         elif x != N-1:
#             return find_mineral(x+1,y)
#         elif y != M-1:
#             return find_mineral(x,y+1)
#         else:
#             return 0
#
# print(find_mineral(0,0))


N,M = map(int,input().split())
area = []
for i in range(N):
    area.append(list(map(int,input().split())))

best_area = []
for i in range(N):
    tmp = []
    for j in range(M):
        if i == 0:
            if j == 0 :
                tmp.append(area[i][j])
            else:
                tmp.append(tmp[j-1]+area[i][j])

        else:
            if j == 0:
                tmp.append(best_area[i-1][j] + area[i][j])
            else:
                tmp.append(max(best_area[i-1][j],tmp[j-1])+area[i][j])
    best_area.append(tmp)

print(best_area[N-1][M-1])
