T = int(input())
for _ in range(T):
    quiz = input()
    cnt = 0
    tmp = 1
    for i in quiz:
        if i == "O":
            cnt += tmp
            tmp += 1
        else:
            tmp = 1
    print(cnt)
