

word_1 = input()
word_2 = input()

cnt_list = [[0 for i in range(len(word_1)+1)]for j in range(len(word_2)+1)]
# print(cnt_list)

for i in range(1,len(word_2)+1):
    for j in range(1,len(word_1)+1):
        if word_2[i-1] == word_1[j-1]:
            cnt_list[i][j] = cnt_list[i-1][j-1]+1
        else:
            cnt_list[i][j] = max(cnt_list[i][j-1],cnt_list[i-1][j])
print(cnt_list[-1][-1])