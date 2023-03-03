def find_max_count(arr,arr_time):
    tmp_arr_time = arr_time[:]
    if len(arr) == 0:
        return 0
    #no = find_max_count(arr[1:],arr_time)
    if arr_time[arr[0][0]] != 1:
        for i in range(arr[0][0],arr[0][1]+1):
            #1은 진행 2는 끝난 시간
            if i == arr[0][1]:
                arr_time[i] = 2
            else:
                arr_time[i] = 1
        #yes = find_max_count(arr[1:],arr_time) + 1
        return max(find_max_count(arr[1:],tmp_arr_time),
                   find_max_count(arr[1:],arr_time) + 1)
    else:
        return find_max_count(arr[1:],tmp_arr_time)

N = int(input())

arr = []
for i in range(N):
    start , finish = map(int,input().split())
    arr.append([start, finish])

arr.sort(key=lambda x:(x[0],x[1]))
find = -1
for i in arr:
    if i[0] == find:
        arr.remove(i)
    else:
        find = i[0]

arr_time = [0]*(max(map(max,arr))+1)

print(find_max_count(arr,arr_time))

