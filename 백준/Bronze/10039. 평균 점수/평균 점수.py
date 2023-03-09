sum = 0
arr = []
for i in range(5):
  n = int(input())
  if n<40:
    sum += 40
  else:
    sum += n
print(int(sum/5))