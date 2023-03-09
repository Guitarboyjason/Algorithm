N = int(input())
houses = [input()for _ in range(N)]

visit = list()
groups = []
for i in range(N):
    for j in range(N):
        if houses[i][j] == '1':
            if [i,j] not in visit:
                stack = list()
                group = list()
                stack.append([i,j])
                while stack:
                    house = stack.pop()

                    if houses[house[0]][house[1]] == '1' and house not in visit:
                        visit.append(house)
                        group.append(house)
                        if house[0] > 0 and house[0] < N-1:
                            if house[1] > 0 and house[1] < N-1:
                                stack.append([house[0]-1,house[1]])
                                stack.append([house[0]+1,house[1]])
                                stack.append([house[0],house[1]-1])
                                stack.append([house[0],house[1]+1])
                            elif house[1] == 0 :
                                stack.append([house[0]-1,house[1]])
                                stack.append([house[0]+1,house[1]])
                                stack.append([house[0],house[1]+1])
                            else:
                                stack.append([house[0]-1,house[1]])
                                stack.append([house[0]+1,house[1]])
                                stack.append([house[0],house[1]-1])
                        elif house[0] == 0:
                            if house[1] > 0 and house[1] < N-1:
                                stack.append([house[0]+1,house[1]])
                                stack.append([house[0],house[1]-1])
                                stack.append([house[0],house[1]+1])
                            elif house[1] == 0 :
                                stack.append([house[0]+1,house[1]])
                                stack.append([house[0],house[1]+1])
                            else:
                                stack.append([house[0]+1,house[1]])
                                stack.append([house[0],house[1]-1])
                        else:
                            if house[1] > 0 and house[1] < N-1:
                                stack.append([house[0]-1,house[1]])
                                stack.append([house[0],house[1]-1])
                                stack.append([house[0],house[1]+1])
                            elif house[1] == 0 :
                                stack.append([house[0]-1,house[1]])
                                stack.append([house[0],house[1]+1])
                            else:
                                stack.append([house[0]-1,house[1]])
                                stack.append([house[0],house[1]-1])
                groups.append(len(group))

groups.sort()
print(len(groups))
for i in groups:
    print(i)


# def DFS(arr,start):
#     visit = list()
#     stack = list()
#     stack.append(start)
#     while stack:
#         node = stack.pop()
#         if node not in visit:
#             visit.append(node)
