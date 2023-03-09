N,K = map(int,input().split())

arr = [i for i in range(N+1)]

arr_tmp = []

indexfinder = 0
while len(arr) != 1:
    for i in range(K):
        indexfinder+=1
        if indexfinder ==  len(arr):
            indexfinder = 1
    arr_tmp.append(arr.pop(indexfinder))
    indexfinder -= 1
print('<',end = '')
for i in range(len(arr_tmp)):
    if i == len(arr_tmp)-1:
        print(arr_tmp[i], end = '')
    else:
        print(arr_tmp[i], end=', ')
print('>')
