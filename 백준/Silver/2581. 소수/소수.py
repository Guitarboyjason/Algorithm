m = int(input())
n = int(input())
arr = []
for i in range(m,n+1):
  tmp = 0
  if i == 1:
    continue
  for j in range(2,i):
    if i%j == 0:
      tmp = 1
      break
  if tmp == 1:
    continue
  arr.append(i)
if len(arr)==0:
  print(-1)
else:
  print(sum(arr))
  print(min(arr))