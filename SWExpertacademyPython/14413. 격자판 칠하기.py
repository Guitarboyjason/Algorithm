import sys
input = sys.stdin.readline

T = int(input())
for test_case in range(1,T+1):
    N,M = map(int,input().split())
    arr = []
    for i in range(N):
        arr.append(input())
    arr_black = []
    arr_white = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] == "#":
                arr_black.append((i+j)%2)
            elif arr[i][j] == ".":
                arr_white.append((i+j)%2)
    is_black_odd = False
    is_breaked = False
    if arr_black[0] == 1:
        is_black_odd = True
    for i in arr_black:
        if is_black_odd and i== 0 or not is_black_odd and i == 1:
            print(f"#{test_case} impossible")
            is_breaked = True
            break
    if not is_breaked:
        for i in arr_white:
            if is_black_odd and i== 1 or not is_black_odd and i == 0:
                print(f"#{test_case} impossible")
                is_breaked = True
                break
    if is_breaked:
        continue
    print(f"#{test_case} possible")
