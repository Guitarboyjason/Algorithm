word = input()
word = word.upper()
a = []
for i in word:
    a.append(word.count(i))
print(a)
if max(a) != a.count(max(a)):
    print("?")
else: 
    print(word[a.index(max(a))])
    