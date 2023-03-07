N,M = map(int,input().split())

guards = [list(input())for _ in range(N)]

position_column = [False for _ in range(N)]
position_row = [False for _ in range(M)]

for i in range(N):
    if "X" in guards[i]:
        position_column[i] = True
for i in range(M):
    include_X = False
    for j in range(N):
        if guards[j][i] == "X":
            include_X = True
    if include_X:
        position_row[i] = True

print(max(position_column.count(False),position_row.count(False)))