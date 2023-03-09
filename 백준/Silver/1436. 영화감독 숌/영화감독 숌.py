N = int(input())

list_66 = []
for i in range(666,6660000):
    num = str(i)
    for j in (range(len(num))):
        if num[j] == "6" and len(num)-1 - j >= 2 and num[j+1] == '6' and num[j+2] == "6":
            list_66.append(i)
            break
    if len(list_66) == N:
        break

print(list_66[-1])
