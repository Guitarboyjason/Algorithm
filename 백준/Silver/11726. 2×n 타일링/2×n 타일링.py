def fibonacci(num):
    if num == 1 or num == 2 : 
        return 1
    else:
        if arr[num]!= 0:
            return arr[num]
        else:
            arr[num] = fibonacci(num-1)+fibonacci(num-2)
            return arr[num]

arr = [0]* 1000
n = int(input())
sum = 1

for i in range(1,n):
    sum += fibonacci(i)

print(sum%10007)