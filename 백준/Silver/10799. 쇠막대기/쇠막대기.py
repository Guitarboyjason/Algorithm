from collections import deque

sticks = input()

arr = deque()
cnt = 0
flag = True
for i in sticks:

    if i == "(":
        arr.append(i)
        flag = True
    if i == ")":
        if flag == True and arr[-1] == "(":
            arr.pop()
            cnt += len(arr)
            flag = False
        else:
            arr.pop()
            cnt += 1
print(cnt)
# (((()(()()))(())()))(()())
#   3
