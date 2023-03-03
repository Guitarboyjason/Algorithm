 #최선이라는게 있잖아?

n = int(input())
stairs = [-1]
max_scores = [-1]*(n+1)
for i in range(n):
    stairs.append(int(input()))
max_scores[0] = 0
for i in range(1,n+1):
    if i == 1 :
        max_scores[i] = stairs[i]
    else:
        if max_scores[i] == max_scores[i-1]:
            
