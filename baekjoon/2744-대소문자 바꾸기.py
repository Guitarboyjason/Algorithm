word = input()
for i in word:
    if i.lower() == i:
        print(i.upper(),end="")
    else:
        print(i.lower(),end="")