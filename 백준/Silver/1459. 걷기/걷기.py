X,Y,W,S = map(int,input().split())

if 2 * W <= S:
    print((X+Y)*W)

else:
    answer = 0
    answer += min(X,Y) * S
    if W > S:
        if abs(X-Y) % 2 == 0:
            answer += abs(X-Y) * S
        else:
            answer += (abs(X-Y)-1) *S + W
    else:
        answer += abs(X-Y) * W
    print(answer)
