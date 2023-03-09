# 몇개를 가지고 있는지 알아내야 한다.
import sys
input = sys.stdin.readline

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
            middle_start = middle
            middle_end = middle
            if middle != 0:
                left_start = 0
                left_end = middle #- 1
                # k = middle
                while left_start <= left_end:
                    left_middle = (left_start + left_end)//2
                    if card[left_middle] == i:
                        left_end = left_middle-1
                        k = left_middle
                    else:
                        left_start = left_middle + 1
                middle_start = k
            if middle != N-1:
                right_start = middle #+ 1
                right_end = N - 1
                # k = middle
                while right_start <= right_end:
                    right_middle = (right_start + right_end)//2
                    if card[right_middle] == i:
                        right_start = right_middle+1
                        k = right_middle
                    else:
                        right_end = right_middle - 1
                middle_end = k
            answer = middle_end - middle_start + 1
            break
            # answer += 1
            # tmp = middle - 1
            # while tmp >= 0 :
            #     if card[tmp] == i:
            #         answer += 1
            #         tmp -= 1
            #     else:
            #         break
            # tmp = middle + 1
            # while tmp<=N-1:
            #     if card[tmp] == i:
            #         answer += 1
            #         tmp += 1
            #     else:
            #         break
            # break

        elif card[middle] > i:
            end = middle -1
        else:
            start = middle + 1
    print(answer,end=" ")
