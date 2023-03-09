def fibonaci(num):
  if num == 0 :
    return 0
  elif num == 1:
    return 1
  else:
    return fibonaci(num-1)+fibonaci(num-2)
n = int(input())
print(fibonaci(n))