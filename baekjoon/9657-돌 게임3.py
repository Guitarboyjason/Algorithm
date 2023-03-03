N = int(input())
player = ["CY","SK"]
# can = [4,3,1]
#돌 1개, 3개, 4개 가져갈 수 있다.
#상근이 먼저 시작
# def stones(N,can):
#     for i in can:
#         if
#승 : 1  패 : 0
stones = [-1] * (N+1)
if N == 1 or N == 3 or N == 4:
    print("SK")
elif N == 2:
    print("CY")
else:
    stones[1] = 1
    stones[2] = 0
    stones[3] = 1
    stones[4] = 1
    for i in range(5,N+1):
        if stones[i-1] == 1 and stones[i-3] == 1 and\
            stones[i-4] == 1:
            stones[i] = 0
        else:
            stones[i] = 1
    print(player[stones[i]])
