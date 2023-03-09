N,M = map(int,input().split())
J = int(input())
M -= 1
fall = [int(input()) for _ in range(J)]
def catch(fall,now):
    if len(fall) == 0:
        return 0
    else:
        if now > fall[0]:       #떨어지는 위치가 현재의 제일 왼쪽부분보다 앞일 때
            return now-fall[0] + catch(fall[1:],fall[0])
        elif now + M > fall[0]:#떨어지는 위치가 현재 받을 수 있을 때
            return 0 + catch(fall[1:],now)
        else:                   #떨어지는 위치가 현재 가장 오른쪽보다 뒤일때
            return fall[0]-(now+M) + catch(fall[1:],fall[0]-M)
print(catch(fall,1))

