from itertools import permutations
from collections import deque

def solution(n):
    step_2 = n//2
    step_1 = n%2
    arr = deque([2]*step_2+[1]*step_1)
    cnt = 0
    for i in range(step_2+1):
        cnt += len(set(permutations(arr)))
        arr.popleft()
        arr.append(1)
        arr.append(1)
    return cnt
# print(set(permutations([1,1,1,1,1])))

print(solution(3))
