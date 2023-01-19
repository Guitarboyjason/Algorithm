# #색종이의 크기는 모두 10*10이다
# #겹치는 부분을 빼면 될 것.

# N = int(input())
# position_arr = []
# for _ in range(N):
#     position_arr.append(list(map(int,input().split())))

# # position_arr.sort()
# # print(position_arr)
# area = N*100
# for i in range(N-1):
#     for j in range(i+1,N):
#         if abs(position_arr[i][0]-position_arr[j][0]) < 10 and\
#             abs(position_arr[i][1]-position_arr[j][1]) < 10:
#             area -=(10-abs(position_arr[i][0]-position_arr[j][0]))*(10- abs(position_arr[i][1]-position_arr[j][1]))
# print(area)

white_area = [[False for _ in range(101)]for _ in range(101)]
N = int(input())
for _ in range(N):
    x_start,y_start = map(int,input().split())
    for i in range(x_start,x_start+10):
        for j in range(y_start,y_start+10):
            white_area[i][j] = True
# print(white_area)
black_area = 0
for i in white_area:
    black_area+=i.count(True)
print(black_area)