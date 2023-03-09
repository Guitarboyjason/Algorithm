a,b,c = map(int,input().split())
x = c-b
if x <= 0:
  print(-1)
else:
  y = a//x
  print(y+1)