# 자연수 N이 주어짐

N = int(input())
arr_N = list(map(int,input().split()))

M = int(input())
arr_M = list(map(int,input().split()))

arr_N.sort()

def find_binary(arr,wantnum):
    if len(arr) == 1:
        if arr[0] == wantnum:
            return 1
        else:
            return 0
    else:
        middle = (len(arr)-1)//2
        if arr[middle] == wantnum:
            return 1
        elif arr[middle] > wantnum:
            return find_binary(arr[:middle])
        else:
            return find_binary(arr[middle+1:])

for i in arr_M:
    print(find_binary(arr_N,i))
