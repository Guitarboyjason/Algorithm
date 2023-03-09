from collections import deque
import sys
input = sys.stdin.readline
AC = ["R","D"]
T = int(input().strip())

for i in range(T):
    p = input().strip()
    n = int(input().strip())
    if n !=0:
        dq = deque(map(int,input().lstrip('[').rstrip(']\n').split(',')))
    else:
        input()
        dq = []
    p = p.replace('RR','')
    # 먼저 오류처리를 해줄까
    swap = False
    error = False
    for i in p:
        if len(dq) == 0 and i == "D":
            error = True
            break
        if i == "R":
            swap = not swap
        if i == "D":
            if swap:
                dq.pop()
            else:
                dq.popleft()

    if error:
        print("error")
    else:
        if swap:
            print(str(list(reversed(dq))).replace(" ",""))
            # print(list(reversed(dq)),)
        else:
            print(str(list(dq)).replace(" ",""))

