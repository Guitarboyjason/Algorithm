import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    note_1 = list(map(int,input().split()))
    M = int(input())
    note_2 = list(map(int,input().split()))

    note_1.sort()
    for i in note_2:
        start = 0
        end = N-1
        answer = 0
        while start <= end:
            middle = (start+end)//2
            if note_1[middle] == i:
                answer = 1
                break
            elif note_1[middle] > i:
                end = middle-1
            else:
                start = middle+1
        print(answer)
