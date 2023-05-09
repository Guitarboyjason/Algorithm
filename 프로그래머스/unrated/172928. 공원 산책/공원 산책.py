def solution(park, routes):
    answer = []
    direction = {"N":(-1,0),"E" : (0,1),"W":(0,-1),"S":(1,0)}
    W = len(park[0])
    H = len(park)
    start_x = [idx for idx,i in enumerate(park) if "S" in i][0]
    # print(start_x)
    start_y = park[start_x].index("S")
    # print(start_y)
    now =[start_x,start_y]
    for i in routes:
        direct,cnt = i.split()
        x,y = now
        cnt = int(cnt)
        nx,ny = direction[direct]
        nx *= cnt
        ny *= cnt
        nx += x
        ny += y
        print(x,y)
        print(nx,ny)
        can_move = True
        if 0<=nx<H and 0<=ny<W:
            print("ready to process")
            for i in range(min(x,nx),max(x,nx)+1):
                if park[i][ny] == "X":
                    can_move = False
                    break
            for j in range(min(y,ny),max(y,ny)+1):
                if park[nx][j] == "X":
                    can_move = False
                    break
            if can_move:
                now = [nx,ny]
    return now