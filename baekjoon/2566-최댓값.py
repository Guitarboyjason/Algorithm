# arr= [list(map(int,input().split()))for _ in range(9)]

# max_value = max(max(i) for i in arr)
# print(max_value)
# for column_index,column in enumerate(arr):
#     if max_value in column:
#         print(column_index+1,column.index(max_value)+1)
#         break

arr = [list(map(int,input().split()))for _ in range(9)]
max_value_and_index = max(list([arr[i][j],i+1,j+1] for i in range(9) for j in range(9)))
# print(max_value_and_index)
print(max_value_and_index[0])
print(*max_value_and_index[1:])
