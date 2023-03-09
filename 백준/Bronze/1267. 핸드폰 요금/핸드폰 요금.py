N = int(input())
arr = list(map(int,input().split()))

cnt_young = 0
cnt_min = 0
for i in arr:
    cnt_young += 10*(i//30+1)
    cnt_min += 15 * (i//60+1)


if cnt_min > cnt_young:
    print("Y {}".format(cnt_young))
elif cnt_young > cnt_min:
    print("M {}".format(cnt_min))
else:
    print("Y M {}".format(cnt_min))
