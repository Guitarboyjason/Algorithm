L,P = map(int,input().split())
arr = list(map(int,input().split()))

guess = L * P
for i in arr:
    print(i - guess,end=" ")
