# croatia = [["č","c="],["ć","c-"],\
#            ["dž","dz="],["đ","d-"],\
#            ["lj","lj"],["nj","nj"],\
#            ["š","s="],["ž","z="]]
croatia = ['c=','c-','dz=','d-','lj','nj','s=','z=']
word = input()
count = 0
while word != "":
    tmp_count = count
    for i in croatia:
        if len(word) >= 2 and i[0] == word[0] and i[1] == word[1]:
            word = word[len(i[1]):]
            count += 1
            break
    if count == tmp_count:
        word = word[1:]
        count += 1
print(count)
