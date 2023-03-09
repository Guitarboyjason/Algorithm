from collections import deque
num = input()
while num != "0":
    num = deque(num)
    while len(num) > 1:
        if num.popleft() != num.pop():
            print("no")
            break
    else:
        print("yes")
    num = input()
    