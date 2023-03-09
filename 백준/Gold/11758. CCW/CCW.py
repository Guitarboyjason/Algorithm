# 반시계 : -1
# 시계 : 1
# 일직선 : 0
P1 = list(map(int,input().split()))
P2 = list(map(int,input().split()))
P3 = list(map(int,input().split()))

answer = (P3[1]-P1[1])*(P2[0]-P1[0])- (P3[0]-P1[0])*(P2[1]-P1[1])
if answer > 0 :
    answer = 1
if answer < 0:
    answer = -1
print(answer)
# 시계방향 : 