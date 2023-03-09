# 14470-전자레인지

# 온도가 0 미만일 때 : 온도가 c초에 1도씩 오른다.
# 얼어있으면서 온도가 0도일때 : 해동하는데 D초가 걸린다.
# 얼어있지 않을 때 e초에 1도씩 오른다.

A = int(input())    #초기 온도
B = int(input())    #목표 온도
C = int(input())    #얼어 있는 고기 데우는 시간
D = int(input())    #고기를 해동하는 데 걸리는 시간
E = int(input())    #얼지 않은 고기를 데우는 데 걸리는 시간

under_zero = 0
over_zero = 0
zero = 0

if A >= 0:
    over_zero = B-A
elif B >= 0:
    over_zero = B
    under_zero = 0 - A
    zero = D
else:
    under_zero = B - A

print(under_zero * C + zero + over_zero * E)
