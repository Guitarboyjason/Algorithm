# from itertools import combinations


def solution(balls, share):
    # balls = [i for i in range(balls)]
    # return len(list(combinations(balls, share)))
    answer = 1
    for i in range(1, balls+1):
        answer *= i
    for i in range(1, share+1):
        answer //= i
    for i in range(1, balls-share+1):
        answer //= i
    return answer


print(solution(3, 2))
