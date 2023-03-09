word = input()
for i in range(26):
    print(word.count(chr(i+97)),end=" ")
