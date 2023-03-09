# 1 1
# 2 5
# 3 9
# 4 13
N = int(input())

star_list = list()
def star(N):
    cnt = (N-1)*4 + 1
    # for i in star_list:
    #     print(i)
    if star_list == []:
        for i in range(cnt):
            if i == 0 or i == cnt-1:
                star_list.append('*'*cnt)
            else:
                star_list.append("*"+" "*(cnt-2) + "*")

    else:
        diff = (len(star_list) - cnt)//2
        for i in range(diff,len(star_list)-diff):
            if i == diff or i == len(star_list)-diff-1:
                # for j in range(cnt):
                star_list[i]= star_list[i][:diff] + '*'*cnt + star_list[i][diff+cnt:]
                # star_list[i][diff:len(star_list)-diff + 1] = ['*'*cnt]
            else:
                star_list[i] = star_list[i][:diff] + "*" + " "*(cnt-2) + "*" + star_list[i][diff+cnt:]
                # for j in range(1,cnt-1):
                #     star_list[i][diff+j] = ' '
                # star_list[i][0] = '*'
                # star_list[i][cnt] = '*'
                # star_list[i][diff:len(star_list)-diff + 1] = ["*"+" "*(cnt-2) + "*"]
    if N != 1:
        star(N-1)

star(N)
# print(star_list)
for i in star_list:
    print(i)
