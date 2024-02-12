"""
오목 결과를 출력하라
검은 바둑알 == 1
흰 == 2
결정 x == 0

검, 흰인 경우 가장 왼쪽에 있는 바둑알 (세로로 놓인 경우 가장 위에 있는 것)(위 먼저 왼쪽)
의 가로줄 번호와 세로줄 번호

"""


def checker(x, y, direction):
    global cnt
    global flag
    global arr
    arr.append((x, y))
    if cnt == 5:
        flag = True
    else:
        flag = False
    nx, ny = direction
    nx += x
    ny += y
    if 0 <= nx < 19 and 0 <= ny < 19 and board[x][y] == board[nx][ny]:
        cnt += 1
        checker(nx, ny, direction)


board = [list(map(int, input().split())) for _ in range(19)]

direction = [
    (i, j) for i in range(-1, 2) for j in range(-1, 2) if not (i == 0 and j == 0)
]

flag = False
for i in range(19):
    for j in range(19):
        if board[i][j] != 0:
            for k in range(8):
                flag = False
                cnt = 1
                nx, ny = direction[k]
                arr = []
                if (
                    (
                        0 <= i - nx < 19
                        and 0 <= j - ny < 19
                        and board[i - nx][j - ny] != board[i][j]
                    )
                    or not 0 <= i - nx < 19
                    or not 0 <= j - ny < 19
                ):
                    checker(i, j, direction[k])

                if flag:
                    print(board[i][j])
                    arr.sort(key=lambda x: x[0])
                    arr.sort(key=lambda x: x[1])
                    print(arr[0][0] + 1, arr[0][1] + 1)
                    break
            if flag:
                break
    if flag:
        break
else:
    print(0)
