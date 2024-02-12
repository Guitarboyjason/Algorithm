# 방향을 다 90도로 바꿔서 위치를 미세조정하는 방식으로 하자
# 90도를 바꾸게 되면 미세조정이 따로 필요할 것 같진 않다. 아니네; 미세조정 필요함
# 그냥 tmp_board를 만들어 이걸 나중에 board에 갖다 붙이는 방식으로 가자.
directions = {0: (0, 1), 1: (-1, 0), 2: (0, -1), 3: (1, 0)}


# 90도로 회전 : x 증가방향 -> y 증가방향, y증가방향 -> x 감소방향
def draw_dragon(x, y, d, g):
    root = (x, y)
    tmp_board = [[0 for _ in range(101)] for _ in range(101)]
    nx, ny = directions[d]
    tmp_board[x][y] = 1
    tmp_board[x + nx][y + ny] = 1
    for i in range(g):
        far_point = root
        far_dis = 0
        for j in range(101):
            for k in range(101):
                if tmp_board[j][k] == 1:
                    tmp = (root[0] - j) ** 2 + (root[1] - k) ** 2
                    if tmp > far_dis:
                        far_dis = tmp
                        far_point = [j, k]
        n_tmp_board = rotate(tmp_board)
        n_tmp_board = [[i for i in j] for j in tmp_board]
        print(n_tmp_board)
        raise


def rotate(tmp_board):
    rotated_board = []
    for i in range(101):
        tmp = []
        for j in range(100, -1, -1):
            tmp.append(tmp_board[j][i])


N = int(input())
board = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(N):
    x, y, d, g = map(int, input().split())
    draw_dragon(x, y, d, g)
