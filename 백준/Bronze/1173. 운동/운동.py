N,m,M,T,R = map(int,input().split())

workout = 0
pulse = m
time = 0
if m+T > M:
    print("-1")
else:
    while workout < N:
        time += 1
        if pulse + T <= M:
            pulse += T
            workout += 1
        else:
            pulse -= R
            if pulse <= m:
                pulse = m
                
    print(time)