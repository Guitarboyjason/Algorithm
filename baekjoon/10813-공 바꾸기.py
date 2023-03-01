N,M = map(int,input().split())
change_balls = [list(map(int,input().split()))for _ in range(M)]
balls = [i for i in range(N+1)]

for i,j in change_balls:
    balls[i],balls[j] = balls[j],balls[i]
print(*balls[1:])