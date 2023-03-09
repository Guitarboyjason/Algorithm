A,B,V = map(int,input().split())
len = A-B
V -= A
if V <= 0:
  print(1)
elif V <= len:
  print(2)
elif V%len == 0:
  print(V//len+1)
else:
  print(V//len+2)