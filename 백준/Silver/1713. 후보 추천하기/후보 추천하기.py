from collections import deque
N = int(input())
int(input())
recommend = list(map(int,input().split()))

students = [10000 for _ in range(101)]
pictures = deque()
for i in recommend:
    if i in pictures:
        students[i] += 1
    elif i not in pictures and len(pictures) < N:
        pictures.append(i)
        students[i] = 1
    else:
        tmp = deque()
        while True:
            compare = pictures.popleft()
            if min(students) == students[compare]:
                students[compare] = 10000
                pictures.extendleft(tmp)
                break
            else:
                tmp.appendleft(compare)
        pictures.append(i)
        students[i] = 1
pictures = list(pictures)
pictures.sort()
for i in pictures:
    print(i, end = " ")
