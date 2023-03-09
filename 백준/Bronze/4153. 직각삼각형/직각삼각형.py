while(True):
    a,b,c = map(int,input().split())
    if a == 0 and b == 0 and c == 0 :
        break
    max = a
    others = [b,c]
    if b > max:
        max = b
        others = [a,c]
    if c > max:
        max = c
        others = [a,b]
    if max**2 == others[0]**2 + others[1]**2:
        print("right")
    else:
        print("wrong")