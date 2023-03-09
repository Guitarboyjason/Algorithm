n = int(input())
arr = [None]*(n+1)
arr[0] = 0
arr[1] = 1
def fibonaci(num):
  if num == 0:
    return arr[0]
  elif num ==1:
    return arr[1]
  elif arr[num] != None:
    return arr[num]
  else:  
    arr[num]=fibonaci(num-1)+fibonaci(num-2)
    return arr[num]
print(fibonaci(n))

