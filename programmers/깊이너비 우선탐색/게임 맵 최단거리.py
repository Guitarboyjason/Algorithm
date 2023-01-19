def solution(maps):
    goal = [len(maps)-1,len(maps[0])-1]
    been = [[False for i in range(len(maps[0]))] for _ in range(len(maps))]
    # print(been)


    answer = 0


    return 0

maps = [[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(solution(maps))

def DFS(maps,now_x,now_y,been,goal,cnt):
    been[now_x][now_y] = True
    queue = []
    if now_x == goal[0] and now_y == goal[1]:
        return cnt
    for index,i in enumerate(maps[now_x]):
        if been[now_x][index] == False:
            queue.append([now_x,index])
            
    # for index,i in enumerate(maps[now_x]):
    #
    #     for jndex,j in enumerate(i):
    #         if been[index][jndex] == False:
    #             return min(DFS(maps,index,jndex,been,goal,cnt+1))
