sentence = input()
cnt = 0
for i in sentence:
    if cnt == 10:
        print()
        print(i, end="")
        cnt = 1
    else:
        print(i,end= "")
        cnt += 1
