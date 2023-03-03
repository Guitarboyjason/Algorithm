from collections import deque

T = int(input())


for test_case in range(1, T+1):
    N = int(input())

    direction_x = deque([1, 0, -1, 0])
    direction_y = deque([0, 1, 0, -1])
    arr = [[-1 for _ in range(N)]for _ in range(N)]
    cnt = 1
    dix = direction_x.popleft()
    diy = direction_y.popleft()
    direction_x.append(dix)
    direction_y.append(diy)
    now_x = 0
    now_y = 0
    arr[now_y][now_x] = cnt
    cnt += 1
    while cnt <= N*N:
        next_x = now_x + dix
        next_y = now_y + diy
        if next_x >= N or next_x < 0 or next_y >= N or next_y < 0 or arr[next_y][next_x] != -1:
            dix = direction_x.popleft()
            diy = direction_y.popleft()
            direction_x.append(dix)
            direction_y.append(diy)
        next_x = now_x + dix
        next_y = now_y + diy
        arr[next_y][next_x] = cnt
        now_x = next_x
        now_y = next_y
        cnt += 1
    print("#{}".format(test_case))
    for i in arr:
        for j in i:
            print(j, end=" ")
        print()
# 음 방향을 체크 하면서 진행 방향이 N을 넘어가거나 0보다 작아지거나
# -1이 아닐 때 방향을 바꿈
