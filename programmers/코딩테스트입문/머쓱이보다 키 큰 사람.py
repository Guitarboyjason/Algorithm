def solution(array, height):
    return len([i for i in array if i > height])
print(solution([149, 180, 192, 170],167))
