from collections import deque

word = deque(input())
while len(word)>1:
    if word.popleft() != word.pop():
        print(0)
        break
else:
    print(1)