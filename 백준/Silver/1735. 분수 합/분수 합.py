a1,b1 = map(int,input().split())

a2,b2 = map(int,input().split())
high = b2 * a1 + b1 * a2
low = b1 * b2
r1 = high
r2 = low
while(r2>0):
    remain = r1%r2
    r1 = r2
    r2 = remain
r = r1
high = high // r
low = low // r
r1 = high
r2 = low
print(high,low)

