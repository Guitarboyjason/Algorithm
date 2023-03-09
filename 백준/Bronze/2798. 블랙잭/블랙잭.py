#각 카드에는 양의 정수
#딜러는 N장의 카드를 모두 보이게 놓고 숫자 M을 외침
#N장의 카드중 3장의 카드를 골라 M을 넘지 않으면서 M과 최대한 가깝게
#M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 출력

#일단 생각 나는건 전체를 다 넣었다 뺐다 해보는 것임.
from itertools import combinations

def find_summary(card,M,cnt):
    if cnt == 0:
        return M
    if len(card) == 0:
        return 300000
    if card[0] <= M:
        return min(find_summary(card[1:],M-card[0],cnt-1),find_summary(card[1:],M,cnt))
    else:
        return 300000
N, M = map(int,input().split())
card = [int(i) for i in input().split()]
card.sort()
print(M-find_summary(card,M,3))
