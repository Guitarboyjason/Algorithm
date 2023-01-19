from collections import deque

#연속된 자연수들의 합으로 나타내야 한다.
#브루트포스로 진행을 해볼까
#이것도 스택이랑 큐로 진행 할 수 있을 것 같은데
def solution(n):
    stack = deque()
    answer = 0
    for i in range(1,n+1):
        stack.append(i)
        while(sum(stack) > n):
            stack.popleft()
        if sum(stack) == n:
            answer += 1

    return answer

print(solution(15))
