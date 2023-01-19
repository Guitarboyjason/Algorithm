def solution(numbers,target):
    answer = 0
    answer += DFS(numbers,target,0)

    return answer

def DFS(numbers,target,summary):
    if len(numbers) == 0:
        if summary == target:
            return 1
        else:
            return 0

    return DFS(numbers[1:],target,summary+numbers[0]) + \
        DFS(numbers[1:],target,summary - numbers[0])

numbers = [1,1,1,1,1]
target =
print(solution(numbers,target))
