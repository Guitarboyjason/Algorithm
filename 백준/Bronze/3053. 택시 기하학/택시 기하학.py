import math
def taxi_geograghic(n):
    sum = 0
    for i in range(n):
        sum += i
    sum = sum * 4 + n*2
    return sum

n = int(input())
print("{:.6f}".format(n*n*math.pi))
print("{:.6f}".format(taxi_geograghic(n)))