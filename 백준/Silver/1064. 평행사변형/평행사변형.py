

# 가장 큰 둘레 길이와 가장 작은 둘레 길이의 차이
# 이걸 도출 해 내려면
# 일단 세 꼭짓점까지의 거리들을 구하고
# 어떤 한 점에서 다른 한 점 까지 x y 의 차를 구해서
# 나머지 한 점에서 같게 구하면 되려나
# 그러면 결국 6개를 만들 수 있다.
# 세 점이 한 선 위에 있으면 평행사변형 불가능
# 굳이 점을 따로 안찍어도 되겠다.
# 그냥 세 점의 거리 차를 하나씩 더 더하면 그게 평행사변형의 둘레
import math
xa, ya, xb, yb, xc, yc = map(int, input().split())

squares = []

if xa == xb == xc or ya == yb == yc:
    answer = -1.0
    print(answer)

elif ya != yb and ya != yc and (xa-xb)/(ya-yb) == (xa-xc)/(ya-yc):
    answer = -1.0
    print(answer)
else:

    dot_length = [math.sqrt((xa - xb)**2 + (ya-yb)**2),
                  math.sqrt((xa - xc)**2 + (ya-yc)**2),
                  math.sqrt((xc - xb)**2 + (yc-yb)**2)]
    answer = (2*max(dot_length) - 2*min(dot_length))

    print("%.16f" % answer)
