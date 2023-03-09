num = [int(x) for x in input().strip().split()]
result = 0
for i in range(len(num)):
    result += num[i] * num[i]
print(result%10)
