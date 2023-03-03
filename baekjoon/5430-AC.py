#R은 배열을 뒤집음
#D는 배열의 첫 수를 버리는 것
from collections import deque
def solve():
    p = input()
    n = int(input())
    arr = input()
    if n == 0 :    #입력 배열이 공백인 경우
        if 'D' in p:
            return 'error'
        else:
            return arr
    arr = arr[1:-1]
    arr = map(int,arr.split(','))
    arr = deque(arr)
    rev = False
    for i in p:
        if i == 'D' and len(arr) == 0:
            return "error"
        if i == 'R':
            if rev == False:
                rev = True
            else:
                rev = False
        else:
            if len(arr) == 0 :
                return "error"
            else:
                if rev == False:
                    arr.popleft()
                else:
                    arr.pop()
    if rev:
        arr.reverse()
    # for i in range(len(arr)):
    #     arr[i] = int(arr[i])
    return list(arr)


T = int(input())
for _ in range(T):
    answer = solve()
    if answer == 'error':
        print(answer)
    else:
        print('[',end='')
        for i in range(len(answer)):
            if i != len(answer)-1:
                print(answer[i],end=',')
            else:
                print(answer[i],end='')
        print(']')


