N,a,b = map(int,input().split())
charming = [list(map(int,input().split()))for _ in range(N)]
a -= 1
b -= 1
jinsu = charming[a][b]
happy = True
for i in range(N):
    if charming[i][b] > jinsu:
        happy = False
    if charming[a][i] > jinsu:
        happy = False
if happy:
    print("HAPPY")
else:
    print("ANGRY")
