#팔아야 이득이 나오는 구조.
#그럼 최대값이 언제인지에 따라 돈을 버는 정도가 다르겠다.
#뒤에부터 차례대로 비교 했을 때 뒤가 앞보다 더 크면 그 때 팔면 됨.
#반대인 경우에는 ?
#뒤집어서 생각

## 마지막이 높은 가격일때 :
    ## 그 전에 나온 가격들이 더 높은 가격일 때:
            #이건 생각 할 필요가 없는게 이미 그때 다 팔고 그다음부터 모으니까
    ## 그 전에 나온 가격들이 다 낮을 때:
            #원기옥 모아서 팔면 됨.
T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    price = list(map(int,input().split()))
    count = 0
    earned_money = 0
    high_price = -1
    for i in range(len(price)-1,-1,-1):
        if high_price < price[i]:
            earned_money += count
            count = 0
            high_price = price[i]
        else:
            count += (high_price - price[i])
    if count != 0:
        earned_money += count

    print(f"#{test_case} {earned_money}")
