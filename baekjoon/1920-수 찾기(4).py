def binary_search(targetNum,start,end,arr):
    if start>end:
        return 0
    mid = (start+end) //2

    if arr[mid] == targetNum:
        return 1
    elif arr[mid] > targetNum:
        end = mid-1
    else:
        start = mid + 1

    return binary_search(targetNum,start,end,arr)

N = int(input())
arr = list(map(int,input().split()))
M = int(input())
find_list = list(map(int,input().split()))
arr.sort()

for i in find_list:
    print(binary_search(i,0,len(arr)-1,arr))

# targetnum == 1
# start = 0, end = 4, mid = 2
# arr[2] = 3 > targetnum
#
