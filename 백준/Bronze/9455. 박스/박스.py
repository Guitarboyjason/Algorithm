T = int(input())
for _ in range(T):
    m, n = map(int,input().split())
    arr_boxes = [list(map(int,input().split())) for _ in range(m)]

    cnt = 0
    while True:
        tmp = cnt
        for i in range(m-2,-1,-1):
            for j in range(n):
                if arr_boxes[i][j] == 1 and arr_boxes[i+1][j] == 0:
                    cnt += 1
                    arr_boxes[i][j] = 0
                    arr_boxes[i+1][j] = 1
        if tmp == cnt:
            break
    print(cnt)
