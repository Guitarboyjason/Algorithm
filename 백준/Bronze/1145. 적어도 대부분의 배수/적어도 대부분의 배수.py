arr = list(map(int,input().split()))
max_num = 1000000
Done = False
for i in range(1, max_num + 1):
    if Done :
        break
    cnt = 0
    for j in arr:
        if i % j == 0:
            cnt += 1
    if cnt >= 3:
        print(i)
        Done = True
        break
