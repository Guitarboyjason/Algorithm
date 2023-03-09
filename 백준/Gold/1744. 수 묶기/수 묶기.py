# 수를 묶을 때 위치와 관계없이 곱한다.
# 그럼 최대한 큰 수들을 묶어주는 것이 좋을 것.
# 묶는 것이 손해인 경우는 어떻게 될까

# N이 50보다 작은 자연수.
# 수는 -1000 보다 크거나 같고 1000보다 작거나 같은 정수이다.

# 그렇다면 음수는 0이하인 수들과 묶어야 하고
# 양수는 양수인 수들과 묶는 것이 좋다.

# 또한 1과 묶이면 오히려 손해
# 음수와 -1은 묶으면 오히려 좋아.

# 정리하자면, 
# 음수+0과 양수를 나누어
# 음수 : 절댓값이 큰 수끼리 곱한다.
# 양수 : 절댓값이 큰 수끼리 곱하는데 1과는 곱하지 않는다.

N = int(input())
nums = [int(input())for _ in range(N)]

list_positive = [i for i in nums if i >= 1]
list_negative = [i for i in nums if i <= 0]
summary = 0

list_positive.sort()
list_positive.reverse()
list_negative.sort()
# print(list_positive)
for i in range(0,len(list_positive)-1,2):
    if list_positive[i] != 1 and list_positive[i+1] != 1:
        summary += list_positive[i] * list_positive[i+1]
        list_positive[i] = 0
        list_positive[i+1] = 0
summary += sum(list_positive)

for i in range(0,len(list_negative)-1,2):
    summary += list_negative[i] * list_negative[i+1]
    list_negative[i] = 0
    list_negative[i+1] = 0
summary += sum(list_negative)

print(summary)