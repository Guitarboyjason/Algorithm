#서로 다른 N개의 자연수의 합이 S.
#N의 최댓값을 구하는 문제
#1,2,3,4.. 더하다보면 S와 비슷해지는 순간이 올 것.
#S를 넘지않는 최대의 합? 을 구성하는 갯수를 구하면 될 것

S = int(input())

sum = 0
count = 0
for i in range(1,S+1):
    sum += i
    count += 1
    if sum > S:
        count -= 1
        break
    elif sum == S:
        break
print(count)
