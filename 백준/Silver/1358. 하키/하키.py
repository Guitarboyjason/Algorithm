#좌표의 절댓값이 정수이므로 근사값으로 비교를 해서 확인을 해 주면 될 것.
#아니다 그냥 반원의 중심부까지의 길이를 구해서 그 길이가 반지름 안에 오는지만 확인하면 될 것임.
import math

W,H,X,Y,P = map(int,input().split())
count = 0
square_X=[X,X+W]
square_Y = [Y,Y+H]
radius = H//2   #H는 짝수라는 조건이 있으므로
for _ in range(P):
    x,y = map(int,input().split())
    if y in range(square_Y[0],square_Y[1]+1):
        if x in range(square_X[0],square_X[1]+1):
            count += 1
        else:
            # if x < square_X[0]: #사실 상관 없지 않을까
            range_point_to_mid = [math.sqrt((x-square_X[0])**2 + (y-(Y+H/2))**2),math.sqrt((x-square_X[1])**2 + (y-(Y+H/2))**2)]
            for i in range_point_to_mid:
                if i <=radius:
                    count += 1
                    break
    else:
        pass
print(count)
