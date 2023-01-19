def solution(n,s):
    if n > s:
        return [-1]
    tmp = s//n
    arr= [tmp]*n
    count = s%n
    for i in range(n-1,n-count-1,-1):
        arr[i] += 1
    return arr

n = 2
s = 8
print(solution(n,s))

