#빨리 뽑는 순서대로 정렬하면 되겠다.

N = int(input())
arr = [int(i) for i in input().split()]

arr.sort()

summary = 0
real_sum = 0
for i in arr:
    summary += i
    real_sum += summary
print(real_sum)
