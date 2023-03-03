#1.한번에 한계단 혹은 두계단을 오를 수 있다.
#2.연속된 세 개의 계단을 밟을 수 없다.
#3.마지막 도착 계단은 반드시 밟아야 한다.

#그럼 역으로 생각해서 마지막 계단부터 생각해보면 어떨까

MININT = -1000000
def scores(stairs, where_from):
    if len(stairs) == 1:
        return stairs[-1]
    elif where_from == 1 and len(stairs) == 2:
        return MININT
    if where_from == 1:
        return stairs[-1] +scores(stairs[:-2],2)
    else:
        return stairs[-1] + max(scores(stairs[:-1],1),\
                                scores(stairs[:-2],2))


n = int(input())
stairs = []
for i in range(n):
    stairs.append(int(input()))

print(scores(stairs,2))
