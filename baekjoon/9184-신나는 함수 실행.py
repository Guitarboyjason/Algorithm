def rec(a, b, c):
    # while a != -1 and b != -1 and c != -1:
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        a, b, c = 20, 20, 20
    if a < b and b < c:
        tmp_a = dpw[a][b][c-1]
        tmp_b = dpw[a][b-1][c-1]
        tmp_c = dpw[a][b-1][c]
        if not tmp_a:
            dpw[a][b][c-1] = rec(a, b, c-1)
        if not tmp_b:
            dpw[a][b-1][c-1] = rec(a, b-1, c-1)
        if not tmp_c:
            dpw[a][b-1][c] = rec(a, b-1, c)
        tmp_a = dpw[a][b][c-1]
        tmp_b = dpw[a][b-1][c-1]
        tmp_c = dpw[a][b-1][c]
        dpw[a][b][c] = tmp_a+tmp_b-tmp_c
    else:
        tmp_a = dpw[a-1][b][c]
        tmp_b = dpw[a-1][b-1][c]
        tmp_c = dpw[a-1][b][c-1]
        tmp_d = dpw[a-1][b-1][c-1]
        if not tmp_a:
            dpw[a-1][b][c] = rec(a-1, b, c)
        if not tmp_b:
            dpw[a-1][b-1][c] = rec(a-1, b-1, c)
        if not tmp_c:
            dpw[a-1][b][c-1] = rec(a-1, b, c-1)
        if not tmp_d:
            dpw[a-1][b-1][c-1] = rec(a-1, b-1, c-1)

        tmp_a = dpw[a-1][b][c]
        tmp_b = dpw[a-1][b-1][c]
        tmp_c = dpw[a-1][b][c-1]
        tmp_d = dpw[a-1][b-1][c-1]
        dpw[a][b][c] = tmp_a+tmp_b+tmp_c-tmp_d
    return dpw[a][b][c]


dpw = [[[False for _ in range(21)]for _ in range(21)]for _ in range(21)]
dpw[0][0][0] = 1
dpw[20][20][20] = 20
a, b, c = map(int, input().split())
while a != -1 or b != -1 or c != -1:
    print("w({}, {}, {}) = {}".format(a, b, c, rec(a, b, c)))
    a, b, c = map(int, input().split())
