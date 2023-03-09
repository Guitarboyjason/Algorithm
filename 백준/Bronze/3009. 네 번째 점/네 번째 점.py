x1, y1 = map(int,input().split())
x2, y2 = map(int,input().split())
x3, y3 = map(int,input().split())
if x1 == x2:
    tmp_x = x3
elif x1 == x3:
    tmp_x = x2
else:
    tmp_x = x1
if y1 == y2:
    tmp_y = y3
elif y1 == y3:
    tmp_y = y2
else:
    tmp_y = y1
print(tmp_x, tmp_y)