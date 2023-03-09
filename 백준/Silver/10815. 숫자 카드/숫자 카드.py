N = int(input())
card = list(map(int,input().split()))
M = int(input())
compare = list(map(int,input().split()))

card.sort()
for i in compare:
    start = 0
    end = N-1
    answer = 0
    while start<=end:
        middle = (start+end)//2
        if card[middle] == i:
            answer = 1
            break
        elif card[middle] > i:
            end = middle -1
        else:
            start = middle + 1
    print(answer,end=" ")
