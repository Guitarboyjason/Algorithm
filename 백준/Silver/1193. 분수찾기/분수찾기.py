def FindN(n):
    sum = 0
    if n == 1:
        return [1,0]
    elif n == 2:
        return [2,1]
    for i in range(0,n):
        sum += i
        if sum >= n:
            break
    return [i,sum-n]
def Answer(answer):
    if answer[0] % 2 == 0:
        print("{}/{}".format(answer[0]-answer[1],1+answer[1]))
    else:
        print("{}/{}".format(1+answer[1],answer[0]-answer[1]))
n = int(input())
answer = FindN(n)
Answer(answer)
