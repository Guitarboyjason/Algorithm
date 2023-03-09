sets = [1,1,2,2,2,8]
have = list(map(int,input().split()))
for i in range(0,6):
    sets[i] -= have[i]
for i in sets:
    print(i ,end=" ")