N,M = map(int,input().split())

put_balls = [list(map(int,input().split()))for _  in range(M)]
balls = [0 for i in range(N+1)]

for start,end,num in put_balls:
    for put in range(start,end+1):
        balls[put] = num
        
print(*balls[1:])
# 1 2 1 1
# 1 2 3 4