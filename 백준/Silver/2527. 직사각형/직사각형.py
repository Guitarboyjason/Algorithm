# a - set했을 때 갯수가 8
# b - set했을 때 갯수가 

# x좌표나 y좌표중 최대값과 최소값을 비교하여 둘다 작거나 둘다 큰 경우 :
# a는 아님
# 이 중 나머지 한 좌표 또한 그런 경우
# c


for _ in range(4):
    line = list(map(int,input().split()))
    square1 = line[:4]
    square2 = line[4:]
    column_checker = 0
    row_checker = 0
    same_column_checker=0
    same_row_checker=0
    if square1[2] < square2[0] or square2[2] < square1[0]:
        column_checker = 1
    if square1[3] < square2[1] or square2[3] < square1[1]:
        row_checker = 1
    if square1[2] == square2[0] or square2[2] == square1[0]:
        same_row_checker = 1
    if square1[3] == square2[1] or square2[3] == square1[1]:
        same_column_checker = 1
    if column_checker or row_checker :
        print("d")
    elif same_column_checker or same_row_checker:
        if same_row_checker and same_column_checker:
            print("c")
        else:
            print("b")
    else:
        print("a")