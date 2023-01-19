def solution(n):
    arr = set(i//2 * 2 for i in range(n+1))
    return sum(arr)
print(solution(4))
