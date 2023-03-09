n_max = 123456
arr = [0] * (2*n_max+1)
arr[0] = -1
arr[1] = -1
def prime(n):
  min = n+1
  max = 2*n
  cnt = 0
  if n == 1:
    return 1
  else:
    for i in range(2,max):
      if arr[i] == -1:
        continue
      else:
        for j in range(2*i,max+1,i):
          arr[j] = -1
    for i in range(min,max+1):
      if arr[i] != -1:
        cnt +=1
    return cnt
n = 1
while n:
  n = int(input())
  if n == 0:
    break
  print(prime(n))
