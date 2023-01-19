from collections import deque

# 구명보트를 최대한 적게 사용하여 모든 사람을 구출하려고 한다.
# 모든 사람을 구출 하기 위해 필요한 구명 보트 개수의 최솟값을 리턴

def solution(people,limit):
    people = deque(sorted(people,reverse=True))
    cnt = 0
    weight = 0

    while(people):
        weight = limit - people.popleft()
        while people and weight - people[-1] >= 0:
            weight -= people.pop()
        cnt += 1
    for i in people:
        weight = 0
    return cnt
people = [70, 80, 50]
limit = 100

print(solution(people,limit))
