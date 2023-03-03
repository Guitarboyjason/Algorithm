N = int(input())
arr = [i for i in range(1,N+1)]
while len(arr)!=1:
    arr.pop(0)
    tmp = arr.pop(0)
    arr.append(tmp)
print(arr[0])
