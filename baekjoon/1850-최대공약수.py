def gcd(a,b):
    if a<b:
        a,b = b,a
    while(b > 0):
        remain = a %b
        a = b
        b = remain
    return a

a,b =map(int,input().split())
answer = "1"*gcd(a,b)
print(answer)
