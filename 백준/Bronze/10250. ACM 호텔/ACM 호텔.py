n = int(input())
for i in range(n):
  h,w,n = map(int,input().split())
  x = n//h
  y = n%h
  if y == 0:
    print(h*100+x)
  else:
    print(y*100 + x+1)