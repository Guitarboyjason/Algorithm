h,m = input().split()
h = int(h)
m = int(m)
if m < 45:
    if h ==0:
        h = 23
    else:
        h -= 1
    m += 15
else:
  m -= 45
print(h,m)
