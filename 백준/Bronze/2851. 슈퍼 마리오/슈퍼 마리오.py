# 점수의 합을 최대한 100에 가깝게 만들려고 한다.
# 마리오가 받는 점수를 출력하라

mushroom = [int(input())for _ in range(10)]
score = 0
for i in mushroom:
    tmp = i
    score += i
    if score > 100:
        break
if score > 100:
    if score - 100 > 100 - (score - tmp) :
        print(score - tmp)
    else:
        print(score)
else:
    print(score)

