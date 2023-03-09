N = int(input())
name = list(input()for _ in range(N))

name.sort()
cnt = 0
tmp = ""
not_tmp = False
print_list = ""
for i in name:
    if i[0] == tmp:
        cnt += 1
    else:
        tmp = i[0]
        cnt = 1
        not_tmp = False
    if cnt >= 5 and not_tmp == False:
        print_list += i[0]
        not_tmp = True
if print_list == "":
    print("PREDAJA")
else:
    print(print_list)
