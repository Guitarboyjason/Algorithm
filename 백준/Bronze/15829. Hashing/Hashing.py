r = 31
ri = 1
M = 1234567891
summary = 0
L = int(input())
word = [i-96 for i in map(ord,list(input()))]
# print(word)
for i in word:
    summary += ri * i
    ri *= r
    ri %= M
print(summary)