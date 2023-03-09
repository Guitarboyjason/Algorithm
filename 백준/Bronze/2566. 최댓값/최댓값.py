arr = [[]for _ in range(9)]
for i in range(9):
    arr[i] = list(map(int,input().split()))

max_num = -1
max_num_index_x = -1
max_num_index_y = -1

for i in range(9):
    for j in range(9):
        if arr[i][j] > max_num:
            max_num = arr[i][j]
            max_num_index_x = i
            max_num_index_y = j
            
print(max_num)
print(max_num_index_x+1,max_num_index_y+1)