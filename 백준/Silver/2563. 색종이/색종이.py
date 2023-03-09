white_area = [[False for _ in range(101)]for _ in range(101)]
N = int(input())
for _ in range(N):
    x_start,y_start = map(int,input().split())
    for i in range(x_start,x_start+10):
        for j in range(y_start,y_start+10):
            white_area[i][j] = True
# print(white_area)
black_area = 0
for i in white_area:
    black_area+=i.count(True)
print(black_area)