# 알파벳 소문자로 이루어진 N개의 단어,
# 길이가 짧은 순으로
# 길이가 같으면 사전 순으로.

N = int(input())
arr_words = []
for _ in range(N):
    arr_words.append(input())

arr_words.sort()
arr_words.sort(key=lambda x : len(x))
tmp = ''
for i in arr_words:
    if tmp != i:
        print(i)
        tmp = i
        
