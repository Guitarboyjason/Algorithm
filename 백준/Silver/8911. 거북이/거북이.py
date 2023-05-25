'''
L,R 은 방향만 바꾼다.
이동한 영역을 계산하려 한다.
거북이가 지나간 영역을 모두 포함할 수 있는 가장 작은 직사각형의 넓이.
X축으로 얼마나 긴가, y축으로 얼마나 긴가를 나타내는 것.
그러면 x와 y의 현황? 만 저장하고 있으면 될 것.
'''
from collections import deque
import sys
input = sys.stdin.readline
direction = deque([(0,1),(1,0),(0,-1),(-1,0)])

for _ in range(int(input())):
    command = input()
    x,y = 0,0
    x_list = set()
    y_list = set()
    x_list.add(0)
    y_list.add(0)
    for c in command:
        if c == "F":
            nx,ny = direction[0]
            x += nx
            y += ny
            
            x_list.add(x)
            y_list.add(y)
        
        if c == "B":
            nx,ny = direction[2]
            x += nx
            y += ny
            
            x_list.add(x)
            y_list.add(y)
        
        if c == "R":
            direction.append(direction.popleft())
        if c == "L":
            direction.appendleft(direction.pop())
            
    x_list = list(x_list)
    y_list = list(y_list)
    print((max(x_list)-min(x_list))*(max(y_list)-min(y_list)))
    