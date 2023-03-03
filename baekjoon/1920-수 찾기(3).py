N = int(input())
arr = list(map(int,input().split()))
M = int(input())
find_list = list(map(int,input().split()))

arr.sort()

def binary_search(arr,targetNum):
    start = 0
    end = len(arr) - 1
    middle_index = end//2

    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        if targetNum == arr[0]:
            return 1
        else:
            return 0


    if targetNum == arr[middle_index]:
        return 1
    elif targetNum < arr[middle_index]:
        start = middle_index+1
    else:
        end = middle_index-1
    return binary_search(arr[start:end+1],targetNum)

for i in find_list:

    print(binary_search(arr,i))
