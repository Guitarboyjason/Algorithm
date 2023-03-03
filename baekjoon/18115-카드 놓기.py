#1.제일 위의 카드 1장을 바닥에 놓는다.
#2.카드가 두장 이상일 때
    #1)위에서 두번째 카드를 바닥에 내려놓는다.
    #2)제일 및에 있는 카드를 바닥에 내려놓는다.
#마지막에 확인 해 보니 위에서부터 1-2-3-4-..-N 순으로 정렬되어 있다.
#그럼 역순으로 다시 돌아가면 되지 않을까
def skill_1(card):
    arr_first.insert(0,card)

def skill_2(card):
    arr_first.insert(1,card)

def skill_3(card):
    arr_first.append(card)

N = int(input())
arr = [i for i in range(1,N+1)]
arr_first = []
arr_skill = input().split()

for i in range(len(arr_skill)-1,-1,-1):
    card = arr.pop(0)
    if arr_skill[i] == '1':
        skill_1(card)
    elif arr_skill[i] == '2':
        skill_2(card)
    else:
        skill_3(card)
for i in arr_first:
    print(i,end=' ')
