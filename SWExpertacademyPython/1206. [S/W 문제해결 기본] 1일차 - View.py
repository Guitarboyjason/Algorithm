T = 10
for test_case in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    count = 0
    for index,i in enumerate(arr):
        if i != 0:
            if i > max(max(arr[index-2:index]),max(arr[index+1:index+3])):
                count += i - max(max(arr[index-2:index]),max(arr[index+1:index+3]))
    print(f"#{test_case} {count}")