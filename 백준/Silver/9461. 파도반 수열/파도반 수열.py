t = int(input())
for i in range(t):
  arr=[1,1,1,2,2]
  N = int(input())
  mok = N//5
  namugi = N%5
  if mok == 0:
    print(arr[namugi-1])

  else:
    for j in range(mok-1):
      for k in range(5):
        arr[k] += arr[k-1]
    for k in range(namugi):
      arr[k] += arr[k-1]
    print(arr[namugi-1])
      


