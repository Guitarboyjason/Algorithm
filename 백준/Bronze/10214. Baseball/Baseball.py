T = int(input())
for _ in range(T):
    Yonsei = 0
    Korea = 0
    for _ in range(9):
        y , k = map(int,input().split())
        Yonsei += y
        Korea += k
    if Yonsei > Korea:
        print("Yonsei")
    elif Korea > Yonsei:
        print("Korea")
    else:
        print("Draw")
