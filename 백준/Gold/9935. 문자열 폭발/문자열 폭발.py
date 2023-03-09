word = input()
boom_word = input()
# while boom_word in word:
#     word = word.replace(boom_word, "")
#     # print(word)
# if word:
#     print(word)
# else:
#     print("FRULA")
stack = []
for i in word:
    stack.append(i)
    if len(stack) >= len(boom_word) and stack[-len(boom_word):] == list(boom_word):
        for _ in range(len(boom_word)):
            stack.pop()
if stack:
    print("".join(stack))
else:
    print("FRULA")
