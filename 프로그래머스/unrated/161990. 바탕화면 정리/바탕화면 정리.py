def solution(wallpaper):
    answer = []
    column = []
    row = []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == "#":
                row.append(i)
                column.append(j)
    answer=[min(row),min(column),max(row)+1,max(column)+1]
    return answer