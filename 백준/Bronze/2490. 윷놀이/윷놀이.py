# 0 - 배
# 1 - 등

# 배 1 - 도
# 배 2 - 개
# 배 3 - 걸
# 배 4 - 윷
# 베 0 - 모
for _ in range(3):
    throw = list(map(int,input().split()))
    case = throw.count(0)
    if case == 0:
        print("E")
    elif case == 1:
        print("A")
    elif case == 2:
        print("B")
    elif case == 3:
        print("C")
    elif case == 4:
        print("D")


