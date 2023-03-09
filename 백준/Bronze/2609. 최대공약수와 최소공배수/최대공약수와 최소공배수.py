def max_div(num1, num2):
  result = 0
  if num1>num2:
    min = num2
    max = num1
  else:
    min = num1
    max = num2
  if max%min == 0:
    return min
  for i in range(1,min+1):
    if max % i == 0 and min % i == 0:
      result = i
  return result

def min_mult(num1,num2):
  if num1>num2:
    min = num2
    max = num1
  else:
    min = num1
    max = num2
  if max%min == 0:
    return max
  return(int((max/max_div(max,min))*min))


n , m = map(int,input().split())
print(max_div(n,m))
print(min_mult(n,m))