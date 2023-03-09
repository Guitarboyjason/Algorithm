#1676 팩토리얼 0의 개수
#10의 배수가 몇번이나 곱해졌는가를 계산하면 쉬울일.
#2와 5의 곱도 생각해야한다.
#2의 배수는 5의배수보다 압도적으로 많으므로 5의배수도 계산하면 될 일
#10의 배수는 결국 5의 배수에 포함되므로 생각할 필요 없다.

N = int(input())
cnt_5=0


for i in range(1,N+1):
    if i%5 == 0:
        if i%25 == 0:
            if i%125 ==0:
                cnt_5 +=1
            cnt_5 += 1
        cnt_5 +=1
print(cnt_5)
