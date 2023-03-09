# 같은 눈이 3개가 나오면 10,000원 + (같은 눈) * 1,000원의 상금
# 같은 눈이 2개만 나오는 경우에는 1,000원 + (같은 눈)*100원의 상금
# 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈) * 100원의 상금

arr = list(map(int,input().split()))

if arr[0] == arr[1] == arr[2]:
    print(10000+arr[0]*1000)
elif arr[0] != arr[1] and arr[1] != arr[2] and arr[0] != arr[2]:
    print(max(arr)*100)
else:
    if arr[0] == arr[1]:
        tmp = arr[0]
    elif arr[1] == arr[2]:
        tmp = arr[1]
    else:
        tmp = arr[0]
    print(1000 + tmp*100)
