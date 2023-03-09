def gcd(x,y):
    div = x%y
    while div>0:
        x = y
        y = div
        div = x%y
    return y
N = int(input())
list = input().split()

for i in range(N):
    list[i] = int(list[i])

A = list[0]

for i in range(1,N):
    if A>=list[i]:
        print(f"{A//gcd(A,list[i])}/{list[i]//gcd(A,list[i])}")
    else:
        print(f"{A//gcd(list[i],A)}/{list[i]//gcd(list[i],A)}")
