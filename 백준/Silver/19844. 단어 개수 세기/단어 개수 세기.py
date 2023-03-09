word = input()
# word_list = word.split()
# print(word_list)
# for i in range(len(word_list)):
#     word_list[i] = word_list[i].split('-')
# print(word_list)
front = ["c", "j", "n", "m", "t", "l", "d", "qu","s"]
word = word.replace('-',' ').split()
collections = ['a','e','i','o','u','h']
cnt = len(word)
for i in word:
    for j in range(len(i)):
        if i[j] == "'":
            if i[:j] in front and i[j+1] in collections:
                cnt += 1

print(cnt)
