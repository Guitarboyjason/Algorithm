from collections import deque

first_deck = deque()

N = int(input())
skill = input().split()
for i in range(1,len(skill)+1):
    if skill[len(skill)-i] == '1':
        first_deck.appendleft(i)
    elif skill[len(skill)-i] == '2':
        first_deck.insert(1,i)
    else:
        first_deck.append(i)
for i in list(first_deck):
    print(i,end=' ')
