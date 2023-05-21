import math

n = int(input())
start = 0
end = n
answer = -1
while start <= end:
    middle = (start + end) // 2
    if middle**2 >= n:
        answer = middle
        end = middle - 1
    else:
        start = middle + 1
print(answer)
