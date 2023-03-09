# N = int(input())
# num_list = [i for i in range(2**31)]
# arr = list(map(int,input().split()))
#
# for i in arr:
#     num_list[i] = -1
# for i in num_list:
#     if i != 0 and i != -1:
#
N = int(input())
arr = list(map(int,input().split()))
arr.sort()

if arr[0] == 1:
    n = 1
    while True:
        if n < len(arr):
            if arr[n] != n+1:
                print(n+1)
                break
        else:
            print(n+1)
            break
        n += 1
else:
    print(1)
