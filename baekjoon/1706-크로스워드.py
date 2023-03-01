R,C = map(int,input().split())

puzzle = list(list(input())for _ in range(R))

word_list = []
tmp = ""
for i in range(R):
    word_list.append(tmp)
    tmp = ""
    for j in range(C):
        if puzzle[i][j] == "#":
            word_list.append(tmp)
        else:
            tmp += puzzle[i][j]
for j in range(C):
    word_list.append(tmp)
    tmp = ""
    for i in range(R):
        if puzzle[i][j] == "#":
            word_list.append(tmp)
        else:
            tmp += puzzle[i][j]
            
word_list = list(set(word_list))
word_list.sort()

for i in word_list:
    if len(i) >= 2:
        print(i)
        break
# print(word_list)
