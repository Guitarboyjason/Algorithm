# def find_max_time(arr,endtime):



N = int(input())

arr = []
for i in range(N):
    start , finish = map(int,input().split())
    arr.append([start, finish])

arr.sort(key=lambda x:x[0])
arr.sort(key=lambda x:x[1])
# tmp_arr = arr[:]
# find = -1
# for i in tmp_arr:
#     if i[0] == find:
#         arr.remove(i)
#     else:
#         find = i[0]

# tmp_arr = arr[:]
# find = arr[-1][1]
# for i in range(1,len(arr)):#range(1,3)
#     if arr[len(arr)-i-1][1] > find: #[1][1], [0][1]
#         tmp_arr.remove(arr[len(arr)-i-1])
#     else:
#         find = tmp_arr[len(arr)-i-1][1]
last = 0
count = 0
for i,j in arr:
    if i >= last:
        count += 1
        last = j
print(count)


