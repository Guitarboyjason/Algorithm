num_list = list(map(int,input().split()))

while num_list != [-1]:
    num_list = num_list[:-1]
    cnt = 0
    for i in num_list:
        if i*2 in num_list:
            cnt += 1
    print(cnt)
    num_list = list(map(int,input().split()))
