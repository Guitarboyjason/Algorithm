def max_div(num1,num2):
  if num1>num2:
    max = num1
    min = num2
  else:
    max = num2
    min = num1
  if max%min ==0:
    return min
  else:
    tmp = 0
    for i in range(1,min+1):
      if max%i == 0 and min%i==0:
        tmp = i
    return tmp
t = int(input())


for i in range(t):
  n,m = map(int,input().split())
  div = max_div(n,m)
  print(int(n*m/div))