from collections import deque
X = int(input())
stick = deque([64])
while sum(stick) is not X:
    if sum(stick) > X:
        tmp = stick.pop()//2
        stick.append(tmp)
        if sum(stick) >= X:
            continue
        stick.append(tmp)
        
print(len(stick))
        
        
        