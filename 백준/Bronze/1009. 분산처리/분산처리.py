T = int(input())

arr_list = [-1,1,4,4,2,1,1,4,4,2]

for _ in range(T):
    a,b = map(int,input().split())
    tmp = a%10
    tmp_num = arr_list[tmp]
    if tmp_num == -1:
        print(10)
    else:
        tmp = b%tmp_num + tmp_num
        tmp_a = a
        for i in range(tmp-1):
            tmp_a *= a
        if tmp_a%10 == 0:
            print(10)
        else:
            print(tmp_a%10)