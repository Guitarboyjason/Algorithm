import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    people = [list(map(int, input().split()))for _ in range(N)]
    for i in people:
        i.append(sum(i))
    people.sort(key=lambda x: x[2])

    now_min = people[0][2]
    tmp_min = people[0][2]
    # cnt = 0
    hired = []
    tmp_hired = []
    # hired.append(people[0])
    for i in people:
        if tmp_min < i[2]:
            now_min = tmp_min
            tmp_min = i[2]
            hired.extend(tmp_hired)
            tmp_hired = []
        if now_min < i[2]:
            flag = True
            for j in hired:
                if j[0] < i[0] and j[1] < i[1]:
                    flag = False
                    break
            if flag:
                tmp_hired.append(i)
            # tmp_min = i[2]
        else:
            hired.append(i)
    print(len(hired))

    # print(people)
